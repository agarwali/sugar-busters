from everything import *


@app.route("/social", methods = ["GET"])
def social():
  return render_template ("social.html")