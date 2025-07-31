from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    rolled = False
    number = None

    if request.method == 'POST':
        number = random.randint(1, 6)
        rolled = True

    return render_template('dice.html', number=number, rolled=rolled)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
