import sys, os
from flask import *
app = Flask(__name__)

if __name__ == "__main__":
  app.run(port=os.environ.get("PORT", 3000))
