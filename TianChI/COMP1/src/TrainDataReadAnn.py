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
    #! input path : type string, whith contain .ann files
    typeofillness = 0
    databasepath = "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/alldata.db"
    AllFiles = [x for x in os.listdir(path) if os.path.isfile(
        path+'/'+x) and os.path.splitext(path+'/'+x)[1] == '.ann']
    Database = sqlite3.connect(databasepath)
    Cursor = Database.cursor()
    Cursor.execute(
        'create table ANNALLWORD (id integer primary key autoincrement, ill text,class text)')
    for x in AllFiles:
        with open(path + '/' + x, 'r') as f:
            for line in f.readlines():
                wordlist = lineProcess(line)
                typeofillness += 1
                classes = wordlist[0]
                illness = wordlist[1]
                order = "insert or ignore into ANNALLWORD (ill, class) values (" + \
                    '\"' + illness + '\"' + ',' + '\"' + classes + '\"' + ')'
                print(order)
                Cursor.execute("%s" % (order))
    Cursor.close()
    Database.commit()
    Database.close()
    return "Read Train.ann data successfully! All type of ill: " + str(typeofillness)
