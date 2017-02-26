from everything import *


@app.route("/checks", methods = ["GET"])
def checks():
  return render_template ("checks.html")