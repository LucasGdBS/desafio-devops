from pydantic import BaseModel, Field

class FilmeSchema(BaseModel):
    titulo: str = Field(..., title="Título do filme", max_length=50)
    diretor: str = Field(..., title="Diretor do filme", max_length=50)
    genero: str = Field(..., title="Gênero do filme", max_length=50)

class FilmeResponse(FilmeSchema):
    id: int