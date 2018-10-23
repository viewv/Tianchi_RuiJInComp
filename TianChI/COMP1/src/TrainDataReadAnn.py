import os
import sqlite3
import tqdm
from tqdm import trange


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


def readAnn(path, dbname):
    #! input path : type string, whith contain .ann files
    databasepath = "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/" + dbname
    AllFiles = [x for x in os.listdir(path) if os.path.isfile(
        path+'/'+x) and os.path.splitext(path+'/'+x)[1] == '.ann']
    Database = sqlite3.connect(databasepath)
    Cursor = Database.cursor()
    Cursor.execute(
        'create table ANNALLWORD (id integer primary key autoincrement, ill text unique,class text)')
    for x in trange(0, len(AllFiles)):
        with open(path + '/' + AllFiles[x], 'r') as f:
            for line in f.readlines():
                wordlist = lineProcess(line)
                classes = wordlist[0]
                illness = wordlist[1]
                order = "insert or ignore into ANNALLWORD (ill, class) values (" + \
                    '\"' + illness + '\"' + ',' + '\"' + classes + '\"' + ')'
                Cursor.execute("%s" % (order))

    Cursor.close()
    Database.commit()
    Database.close()
    return "Read Train.ann data successfully!"
