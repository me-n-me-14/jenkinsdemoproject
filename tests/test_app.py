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

def test_roll_dice(client):
    rv = client.post('/')
    assert b'You rolled a' in rv.data
    # Check for two numbers from 1 to 6
    assert any(f'You rolled a {i} and a {j}'.encode() in rv.data for i in range(1, 7) for j in range(1, 7))