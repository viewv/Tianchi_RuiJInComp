import jieba
import os
import sqlite3


def classfi(start, end, word, tag, knowdatabasepath):
    konwdataconn = sqlite3.connect(knowdatabasepath)
    konwcour = konwdataconn.cursor()
