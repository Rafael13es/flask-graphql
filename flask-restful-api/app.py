"""APP"""
from flask import Flask, jsonify, Blueprint

app = Flask(__name__)


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    """Welcome"""
    return "Hello World!"


@app.route('/<int:number>/')
def incrementer(number):
    """Incrementer"""
    return "Incremented number is " + str(number + 1)


@app.route('/person/')
def hello():
    """Hello"""
    return jsonify({'name': 'Jimit',
                    'address': 'India'})


@app.route('/numbers/')
def print_list():
    """
    print list
    :return:
    """
    return jsonify(list(range(5)))


@app.route('/home/')
def home():
    """Home"""
    return "Home page"


@app.route('/contact')
def contact():
    """Contact"""
    return "Contact page"


@app.route('/teapot/')
def teapot():
    """Teapot"""
    return "Would you like some tea?", 418


@app.before_request
def before():
    """Before"""
    print("This is executed BEFORE each request.")


@app.route('/x/2')
def hello2():
    """Hello 2"""
    return "Hello World!"


home_bp = Blueprint('home', __name__)


@home_bp.route('/hello/')
def hello3():
    """Hello 3"""
    return "Hello from Home Page"


if __name__ == '__main__':
    app.register_blueprint(home_bp, url_prefix='/home')
    app.run(host='0.0.0.0', port=105)
