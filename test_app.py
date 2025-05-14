import pytest
import json
from app import app

@pytest.fixture
def client():
       app.config['TESTING'] = True
       with app.test_client() as client:
           yield client

def test_hello(client):
       rv = client.get('/hello')
       assert rv.status_code == 200
       assert json.loads(rv.data)['message'] == 'Hello, World!'