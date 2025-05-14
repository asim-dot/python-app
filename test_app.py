import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    rv = client.get('/tasks')
    assert rv.status_code == 200
    assert len(json.loads(rv.data)) >= 2

def test_get_task(client):
    rv = client.get('/tasks/1')
    assert rv.status_code == 200
    assert json.loads(rv.data)['title'] == 'Buy groceries'

def test_create_task(client):
    rv = client.post('/tasks', json={'title': 'Test task'})
    assert rv.status_code == 201
    assert json.loads(rv.data)['title'] == 'Test task'