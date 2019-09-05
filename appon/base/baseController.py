
from flask import Flask, session, redirect, url_for,request,render_template,make_response
import cgi

from appon.config.base import *


def isLogin():
    if 'username' not in session:
        return False
    else:
        return True

