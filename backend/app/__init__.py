from flask import Flask
from config import Config

app = Flask(__name__, template_folder="template")
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'you-will-never-guess'
mtd_api_key = 'd6f508505e3c436daebe0290edce3903'
maps_api_key = 'AIzaSyDLxgV4_-ZOAX2q-hDvPa05qLP27veSzJU'

from app import routes