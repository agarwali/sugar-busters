from everything import *


@app.route("/", methods = ["GET"])
def register():
  return render_template ("register.html")