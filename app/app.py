from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dice_result = None
    if request.method == 'POST':
        dice_result = random.randint(1, 6)
    return render_template('index.html', dice=dice_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
