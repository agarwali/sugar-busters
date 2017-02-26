from everything import *


@app.route("/list", methods = ["GET"])
def lists():
  return render_template ("list.html")