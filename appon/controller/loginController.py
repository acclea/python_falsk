from appon.base.baseController import *

import appon.model.adminModel as adminModel

def doLogin():
    if isLogin():
        return "is login"

    # if request.method != 'POST':
    #     return  "not allow method"


    username = request.form['username']
    if username  == False:
        return "username is empty"

    pwd = request.form['pass']
    if pwd == False:
        return "pass is empty"
    adminWhere  = "status = 1 AND name = '"+ username + "'"
    adminFiled  = "*"
    adminInfo   = adminModel.adminRow(adminWhere,adminFiled)

    if adminInfo == False :
        return "this user is not exist or forbid "



    # 可以设置session有效期
    session.permanent = True
    session["username"] = username
    session["userid"]   = adminInfo['id']

    # 登陆跳转
    return redirect(url_for('home'))
