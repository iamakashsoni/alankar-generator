from flask import Flask, render_template, request

from generate_sargam import generate_sargam

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    swar_notation = request.form['hidden_swar_notation']
    aroh, avaroh = generate_sargam(swar_notation)

    return render_template('result.html', aroh=aroh, avaroh=avaroh)

if __name__ == '__main__':
    app.run(debug=True)
