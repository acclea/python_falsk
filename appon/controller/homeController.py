from appon.base.baseController import *

def logout():
    session.clear()
    return redirect(url_for('login'))