from appon.base.baseController import *

import appon.controller.loginController as LoginC
import appon.controller.homeController as HomeC

app = Flask(__name__,template_folder='appon/view/',static_folder="",static_url_path="")
# app = Flask(__name__)
app.debug = True


# 设置session加密key
app.secret_key = secret_key


@app.route('/')
def index():
    if isLogin():
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('login/index.html')


@app.route('/doLogin',methods=['GET', 'POST'])
def doLogin():
    return LoginC.doLogin()


@app.route('/home')
def home():
    return render_template('home/index.html')


@app.route('/logout')
def logout():
    return HomeC.logout()


if __name__ == '__main__':
    app.run()