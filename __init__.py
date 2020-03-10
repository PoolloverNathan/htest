import sys, os
from flask import *
app = Flask(__name__)

@app.route("/page/<id>", methods=["GET"])
def getpage(id):
  try:
    with f as open(f"pages/<id>", "r"):
      f.seek(0,2)
      s = f.tell()
      f.seek(0,0)
      return f.read(s)
  except OSError:
    return "", 404

if __name__ == "__main__":
  app.run(port=os.environ.get("PORT", 3000))
