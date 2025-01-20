import pytest

@pytest.mark.asyncio
async def test_status_200_when_fetch_all(async_client):
    response = await async_client.get('/filmes')
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_status_200_when_post_filme(async_client):
    data = {
        "titulo": "Matrix",
        "diretor": "Lana Wachowski",
        "genero": "Ficção Científica",
    }
    response = await async_client.post('/filmes', json=data)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_status_200_when_fetch_one(async_client, post_data):
    response = await async_client.get('/filmes/1')
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_status_200_when_update_filme(async_client, post_data):
    id = post_data['id']
    data = {
        "titulo": "Matrix Reloaded",
        "diretor": "Lana Wachowski",
        "genero": "Ficção Científica",
    }
    response = await async_client.patch(f'/filmes/{id}', json=data)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_status_200_when_delete_filme(async_client, post_data):
    id = post_data['id']
    response = await async_client.delete(f'/filmes/{id}')
    assert response.status_code == 200
