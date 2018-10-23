import os
import sqlite3
import tqdm
from tqdm import trange


def datewriter(tag, type, start, end, word, path, filename):
    with open(path + '/' + filename+".ann", 'a') as f:
        newline = [tag, type, start, end, word]
        newline = '\t'.join(newline) + '\n'
        f.write(newline)


def dataopener(dbpath, path, dataname):
    connection = sqlite3.connect(dbpath)
    database = connection.cursor()

    #!start code block
    ID = database.execute("select id from " + dataname)
    # ?Their assume sql is in below format
    # ?id|tag|filename|type|start|end|word
    print("Start Writing ann file")
    for x in ID:
        database.execute(
            "select id from " + dataname + "where id==%d" % (x))
        dataline = (database.fetchall())[0]
        tag = dataline[1]
        filename = dataline[2]
        type = dataline[3]
        start = dataline[4]
        end = dataline[5]
        word = dataline[6]
        datewriter(tag, type, start, end, word, path, filename)
    print("Finish transfor data into ann file")
    #!end code block

    database.close()
    connection.commit()
    connection.close()
