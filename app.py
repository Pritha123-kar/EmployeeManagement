from flask import Flask, render_template

# Create Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to Employee Management Portal!"

# Health check route
@app.route('/health')
def health():
    return {
        "status": "success",
        "message": "Employee Management Portal is running!"
    }

# Run Flask application
if __name__ == '__main__':
    app.run(debug=True)

hello
