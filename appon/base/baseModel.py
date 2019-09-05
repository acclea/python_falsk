import pymysql
import mysql.connector
import mysql
# import appon.config.db as dbConf
from appon.config.db import *


# from  flask_sqlalchemy import  SQLAlchemy
# appon = Flask(__name__)

# def connDB():
#     appon.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/game_data?charset=utf8'
#     # 该配置为True,则每次请求结束都会自动commit数据库的变动
#     appon.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#     appon.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#
#     return  SQLAlchemy(appon)

'''
    ------------------------------------------
    连接MySQL数据库
    
    sql         sql语句
    execType    操作类型，select、insert、update，暂不支持 delete 操作
    fetchType   针对查询（select）操作，one、many、all
    fetchNum    当 fetchType 为 many 时需要传参，正整型
    isexecMnay  当 execType 为 insert、update 时需要传参，bool类型， True/False
    ------------------------------------------
'''
def connDB(sql,execType = 'select',fetchType = 'one',fetchNum = 1,isexecMnay = False):

    # 如果sql不存在
    if sql == False :
        return  False
    # db = mysql.connector.connect("localhost", "root", "root", "game_data")

    conn = mysql.connector.connect(**dbInfo)
    # return db
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor(dictionary = True)

    # 使用 execute()  方法执行 SQL 查询
    # ver = cursor.execute("SELECT VERSION()")
    # return ver
    # 创建连接
    # conn = pymysql.connect(db='game_data', user='root', passwd='root', unix_socket="/tmp/mysql.sock")
    # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root',db='game_data',charset='utf8')
    # conn = pymysql.connect(*dbInfo)

    # 创建游标
    # cursor = conn.cursor(dictionary=True)

    # 设置字符集
    # cursor.execute('SET CHARACTER SET utf8;')

    # 执行写入SQL，并返回受影响行数，使用占位符 实现动态传参
    # effect_row = cursor.execute("insert into user (name) values (%s) ", ('323'))
    # effect_row = cursor.executemany("insert into user (name) values (%s) ",[('123',), ('456',), ('789',), ('0',), ('1',), ('2',), ('3',)])

    # 执行更新多个SQL，并返回受影响行数，列表中每个元素都相当于一个条件
    # effect_row = cursor.executemany("update user set name = %s WHERE  id = %s", [("fuzj", 1), ("jeck", 2)])

    # 使用游标的lastrowid方法获取
    # new_id = cursor.lastrowid

    # 查询
    if execType == "select" :
        cursor.execute(sql)

        if fetchType == "one" :
            ref = cursor.fetchone()
            # print(ref)
            # return ref
        elif  fetchType == "many" :
            ref = cursor.fetchmany(fetchNum)

        else:
            ref = cursor.fetchall()

    # 写入
    elif execType == "insert" :
        if isexecMnay != False :
            cursor.executemany(sql)
            # new_id = cursor.lastrowid
            ref = True
        else:
            cursor.execute(sql)
            ref = cursor.lastrowid

    # 修改
    elif execType == "update" :
        if isexecMnay != False :
            cursor.executemany(sql)
            ref = True
        else:
            cursor.execute(sql)
            ref = True

    # 提交
    conn.commit()

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()

    return  ref

def tables(tb):
    # return dbConf['table_pre']+tb
    return "gm_"+tb