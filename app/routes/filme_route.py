from fastapi import APIRouter
from fastcrud import FastCRUD, crud_router
from app.config.db import get_session
from app.models.filme import Filme
from app.schemas.filme_schema import FilmeSchema

router = APIRouter()

filme_crud = FastCRUD(Filme)
filme_router = crud_router(
    session=get_session,
    model=Filme,
    create_schema=FilmeSchema,
    update_schema=FilmeSchema,
    crud=filme_crud,
    path="/filmes",
    tags=["Filmes"]
)

router.include_router(filme_router)
