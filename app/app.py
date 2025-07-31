from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return render_template('dice.html', dice1=dice1, dice2=dice2, total=total)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
