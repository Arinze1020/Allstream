from flask import Flask

app = Flask(__name__,instance_relative_config=False)
app.config.from_pyfile('config.py')
#app.config['SECRET_KEY'] = 'SECRETKEY'

from app import routes