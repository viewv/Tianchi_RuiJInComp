import os
import sqlite3


def datewriter(tag, type, start, end, word, path, filename):
    with open(path + '/' + filename+".ann", 'a') as f:
        newline = [tag, type, start, end, word]
        newline = '\t'.join(newline) + '\n'
        f.write(newline)


def dataopener(dbpath, path):
    connection = sqlite3.connect(dbpath)
    database = connection.cursor()
    #!start code block

    #!end code block
    database.close()
    connection.close()
