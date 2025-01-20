import pytest_asyncio
from faker import Faker
from sqlalchemy.orm import sessionmaker
from httpx import AsyncClient, ASGITransport
from testcontainers.postgres import PostgresContainer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.main import app
from app.config.base import Base
from app.config.db import get_session

BASE_URL = 'http://localhost:8000'
faker = Faker()

# Fixture to create a postgres container
@pytest_asyncio.fixture
def postgres_container():
    with PostgresContainer('postgres:16', driver='asyncpg') as postgres:
        yield postgres

# Fixture to create a sqlalchemy async session 
@pytest_asyncio.fixture
async def async_session(postgres_container):
    async_db_url = postgres_container.get_connection_url().replace('postgres://', 'postgresql+asyncpg://')
    async_engine = create_async_engine(async_db_url, pool_pre_ping=True, echo=True)

    # Create all tables
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async_session = sessionmaker(
        autoflush=False,
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session

@pytest_asyncio.fixture
async def async_client(async_session):
    app.dependency_overrides[get_session] = lambda: async_session
    _transport = ASGITransport(app)

    async with AsyncClient(transport=_transport, base_url=BASE_URL) as client:
        yield client
    
    app.dependency_overrides.clear()

@pytest_asyncio.fixture
async def post_data(async_client):
    data = {
        "titulo": faker.pystr(),
        "diretor": faker.name_female(),
        "genero": faker.word(),
    }
    response = await async_client.post('/filmes', json=data)
    return response.json()
