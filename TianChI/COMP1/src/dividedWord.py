import jieba
import thulac
import os
import TrainDataReadAnn
import dataFormter
import sqlite3
import tqdm
from tqdm import trange


def delNoUseWord(word="", tag=""):
    pass


def divided(path, knowdatabasepath):
    # TODO:read passage
    # func(readpassage) readline()
    #!return string
    AllFiles = [x for x in os.listdir(path) if os.path.isfile(
        path + '/' + x) and os.path.splitext(path + '/' + x)[1] == '.txt']
    for x in trange(0,len(AllFiles)):
        with open(path+'/'+x) as f:
            f.read()
            

    # TODO:jieba divideword
    # get string
    #!return word list

    # TODO:dateFormat
    # get word and tag and location
    #!return ann document

    # TODO:Remember to close all connection!
