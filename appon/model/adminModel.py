# from appon.base.baseModel import *

import appon.base.baseModel as baseModel

def adminRow(where,filed,order = 'id DESC'):
    table = baseModel.tables("admin")
    sql = "SELECT " + filed + " FROM " + table + " WHERE " + where + " ORDER BY " + order

    adminInfo = baseModel.connDB(sql)
    return adminInfo