from flask import Flask, render_template, request

app = Flask(__name__)

base_url = 'https://api.exchangerate-api.com/v4/latest/'

API_URLS = {
    
}

@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
