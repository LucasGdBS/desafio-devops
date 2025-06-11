from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import filme_route
from app.config.db import lifespan


app = FastAPI(
    lifespan=lifespan,
    title="CRUD FILMES"
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(filme_route.router)
