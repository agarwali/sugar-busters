from everything import *


@app.route("/login", methods = ["GET"])
def login():
  return render_template ("login.html")