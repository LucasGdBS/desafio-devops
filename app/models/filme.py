from app.config.base import Base
from sqlalchemy import Column, Integer, String

class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    diretor = Column(String, nullable=False)
    genero = Column(String, nullable=False)

    def __init__(self, titulo, diretor, genero):
        self.titulo = titulo
        self.diretor = diretor
        self.genero = genero

    def __repr__(self):
        return f'<Filme {self.titulo}>'