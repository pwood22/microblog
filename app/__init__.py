from flask import Flask
from config import Config

app = Flask(__name__) #
app.config.from_object(Config) # This will load the config.py file

from app import routes  # noqa: E402, F401
