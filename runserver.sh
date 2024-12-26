#!/bin/sh

if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python -m venv venv
fi
source venv/Scripts/activate

# Instala as dependências
pip install -r requirements.txt

uvicorn app.main:app --host 0.0.0.0 --port 8000
