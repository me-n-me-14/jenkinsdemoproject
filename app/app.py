from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    rolled = False
    dice1 = None
    dice2 = None

    if request.method == 'POST':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        rolled = True

    return render_template('dice.html', dice1=dice1, dice2=dice2, rolled=rolled)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
