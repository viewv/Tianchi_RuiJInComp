import jieba
import os
import sqlite3


def readAllwords(path):
    # ?Their assume sql is in below format
    # ?id|tag|filename|start|end|word
    possiblewordconn = sqlite3.connect(path)
    possiblewords = possiblewordconn.cursor() 
    #! Code begin
    
    #! Code finish close ALL
    possiblewords.close()
    possiblewordconn.commit()
    possiblewordconn.close()


def classfi(start, end, word, tag, knowdatabasepath):
    konwdataconn = sqlite3.connect(knowdatabasepath)
    konwcour = konwdataconn.cursor()
