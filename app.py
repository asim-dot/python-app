from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD Pipeline! This change was automatically deployed."

@app.route('/about')
def about():
    return "This is a Flask application deployed with Jenkins CI/CD pipeline."

@app.route('/contact')
def contact():
    return "<h1>Contact Us</h1><p>Email: example@example.com</p><p>Phone: (123) 456-7890</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
