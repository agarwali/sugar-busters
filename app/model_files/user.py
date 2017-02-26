from models import *
from university import *


def register(in_email, password, fName, lName):
    user = User(
        email = in_email,
        pwrd = password,
        auth = 0,
        f_name = fName,
        l_name = lName,
        uni_id = get_uni_id(strip_unitag(in_email))
        )
    try:
        user.save()
        return True
    except:
        return False