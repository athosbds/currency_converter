from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)

@app.route('/converter')
def index():
    return render_template('models.py')
