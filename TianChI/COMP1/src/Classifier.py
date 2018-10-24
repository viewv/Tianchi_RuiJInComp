import jieba
import os
import sqlite3
import jieba.posseg as pseg
import tqdm
from tqdm import trange


def judgement():

    # ?Their assume sql is in below format
    # ?ill|class
    trainconn = sqlite3.connect(
        "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/TrainDataAnn.db")
    train = trainconn.cursor()

    # ?Their assume sql is in below format
    # ?id|tag|filename|start|end|word
    testconn = sqlite3.connect(
        "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/noclasswordatebase.db")
    test = testconn.cursor()

    # ?Their assume sql is in below format
    # ?id|tag|filename|type|start|end|word
    ansconn = sqlite3.connect(
        "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/ans.db")
    ans = ansconn.cursor()
    ans.execute(
        "create table ANS (id integer primary key autoincrement, tag text,filename text, type text, start integer, end integer, word text unique)")

    #! Code begin
    cixinset = {'a', 'Ag', 'ad', 'an', 'f', 'm', 'Ng', 'n', 'nz',
                'q', 's', 'tg', 't', 'vg', 'v', 'vd', 'vn', 'z', 'un'}
    test.execute("select id from ALLPOSSIBLE")
    testallid = [x[0] for x in (test.fetchall())]
    jieba.load_userdict(
        "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/dict.txt")
    for x in testallid:
        test.execute("select * from ALLPOSSIBLE " + "where id == %d" % (x))
        dataline = (test.fetchall())[0]
        word = dataline[5]
        filename = dataline[2]
        tagid = dataline[1]
        start = dataline[3]
        end = dataline[4]
        word = pseg.cut(word)
        wordinfo = next(word)
        word = wordinfo.word
        flag = wordinfo.flag
        train.execute(
            "select * from ANNALLWORD where ill glob \'*%s*\'" % (word))
        temp = train.fetchall()
        if len(temp) != 0:
            temp = temp[0]
            tag = temp[2]
        elif (len(temp) == 0):
            continue
        else:
            # cixinset = {'a', 'Ag', 'ad', 'an', 'f', 'm', 'Ng', 'n', 'nz',
            # q', 's', 'tg', 't', 'vg', 'v', 'vd', 'vn', 'z', 'un'}
            if flag in cixinset:
                if flag == 'a':
                    tag = 'Symptom'
                if flag == 'Ag':
                    tag = 'Symptom'
                if flag == 'ad':
                    tag = 'Symptom'
                if flag == 'an':
                    tag = 'Disease'
                if flag == 'f':
                    tag = 'Anatomy'
                if flag == 'm':
                    tag = 'Amount'
                if flag == 'Ng':
                    tag = 'SideEff'
                if flag == 'n':
                    tag = 'Disease'
                if flag == 'nz':
                    tag = 'Drug'
                if flag == 'q':
                    tag = 'level'
                if flag == 's':
                    tag = 'Anatomy'
                if flag == 'tg':
                    tag = 'Duration'
                if flag == 't':
                    tag = 'Duration'
                if flag == 'vg':
                    tag = 'Method'
                if flag == 'v':
                    tag = 'Test'
                if flag == 'vd':
                    tag = 'Operation'
                if flag == 'vn':
                    tag = 'Test'
                if flag == 'z':
                    tag = 'level'
                if flag == 'un':
                    tag = 'Drug'
        ans.execute(
            "insert or ignore into ANS (tag, filename, type, start, end, word) values (\'%s\',\'%s\',\'%s\', %d ,%d,\'%s\')" % (tagid, filename, tag, start, end, word))

    #! Code finish close ALL
    train.close()
    trainconn.close()
    test.close()
    testconn.close()
    ansconn.commit()
    ans.close()
    ansconn.close()
    return "All Done!"
