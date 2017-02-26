from everything import *


@app.route("/source", methods = ["GET"])
def source():
  return render_template ("source.html")