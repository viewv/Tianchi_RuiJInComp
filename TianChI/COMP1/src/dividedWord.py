import jieba
import thulac
import os
import TrainDataReadAnn
import dataFormter
import sqlite3
import tqdm
from tqdm import trange


def divided(path):
    # TODO:read passage
    # func(readpassage) readline()
    #!return string
    AllFiles = [x for x in os.listdir(path) if os.path.isfile(
        path + '/' + x) and os.path.splitext(path + '/' + x)[1] == '.txt']
    jieba.load_userdict(
        "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/dict.txt")

    noclasswordatabase = sqlite3.connect(
        "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/noclasswordatebase.db")
    nodatabase = noclasswordatabase.cursor()

    # ?Their assume sql is in below format
    # ?id|tag|filename|start|end|word
    nodatabase.execute(
        "create table ALLPOSSIBLE (id integer primary key autoincrement, tag text ,filename text ,start integer ,end integer ,word text unique)")

    print("Start Divided Words")
    for x in trange(0, len(AllFiles)):
        possiblewordcount = 0
        with open(path+'/'+AllFiles[x], 'r') as f:
            passage = f.read()
            result = jieba.tokenize(passage)
            for tk in result:
                possiblewordcount += 1
                word = tk[0]
                start = tk[1]
                end = tk[2]
                if word == '\"' or word == "\'":
                    continue
                else:
                    nodatabase.execute(
                        "insert or ignore into ALLPOSSIBLE (tag, filename, start, end, word) values ('%d','%s','%d','%d',\"%s\")" % (possiblewordcount, AllFiles[x], start, end, word))

    # TODO:Remember to close all database connection!
    nodatabase.close()
    noclasswordatabase.commit()
    noclasswordatabase.close()
    return "Finish Divided the word"
