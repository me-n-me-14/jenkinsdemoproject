from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/dice', methods=['GET', 'POST'])
def dice():
    number = None
    if request.method == 'POST':
        number = random.randint(1, 6)
    return render_template('dice.html', rolled=bool(number), number=number)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
def test_dice_route(client):
    response = client.get('/dice')
    assert response.status_code == 200
