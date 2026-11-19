from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to Employee Management Portal!"

# Run application
if __name__ == '__main__':
    app.run(debug=True)
