from flask import Flask

app = Flask(__name__,template_folder="../templates",static_folder="../static")

from app.views import *

if __name__ == "__main__":
    app.run()