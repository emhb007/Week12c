from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MYSECRETKEY'

from application import routes
