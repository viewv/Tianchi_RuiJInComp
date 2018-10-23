import os
import sqlite3


def lineProcess(line):
    line = line.split()
    classes = line[1]
    #!['T14', 'Disease', '10415', '10416;10417', '10421', '2', '型糖尿病']
    temp = line[3]
    temp = temp.split(';')
    if len(temp) == 1:
        illness = ''.join(line[4:])
        return [classes, illness]
    else:
        illness = ''.join(line[5:])
        return [classes, illness]


def readAnn(path):
    AllFiles = [x for x in os.listdir('.') if os.path.isfile(
        x) and os.path.splitext(x)[1] == '.ann']
    Database = sqlite3.connect('aldata.db')
    Cursor = Database.cursor()
    Cursor.execute(
        'create table ANNALLWORD (id integer primary key autoincrement, ill text,class text)')
    for x in AllFiles:
        with open(path + '/' + x, 'r') as f:
            for line in f.readlines():
                wordlist = lineProcess(line)
                classes = wordlist[0]
                illness = wordlist[1]
                Cursor.execute(
                    'insert or ignore into ANNALLWORD (ill, class) values (\'%s\', \'%s\')' % (illness, classes))
