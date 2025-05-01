from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return "Hello from Azure Web App! This is a Python Flask demo.Is this working?"
    
    @app.route('/about')
    def about():
        return "This is the about page of our demo app."
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)