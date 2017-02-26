from everything import *
from datetime import datetime, timedelta

@app.route("/profile", methods = ["GET"])
def profile():
  user = (User.select()
              .join(Physician)
              .where(User.fName == "Ishwar")
          )
  user = user.get()
  now = datetime.now()
  duration = now - user.lastChecked
  td = timedelta(days=180)
  print td
  return render_template ("profile.html",
                            user = user,
                            duration = duration
                          )