import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dice_game(client):
    rv = client.get('/')
    assert b'Dice Roller' in rv.data
    assert b'Roll the Dice' in rv.data
