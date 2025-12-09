from flask import Flask

app = Flask(__name__)

@app.route('/') 
def index():
    return f'<h1>Hello world</h1>'

@app.route('/name')
def name():
    return f'<h1>Thanaphat Ponsang</h1>'

# if __name__ == '_main_':
    # app.run(debug=True)