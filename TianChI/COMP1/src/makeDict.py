import sqlite3
import os
import tqdm
from tqdm import trange

connect = sqlite3.connect(
    "/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/TrainDataAnn.db")
database = connect.cursor()

with open("/home/viewv/Tianchi_RuiJInComp/TianChI/COMP1/src/dict.txt", 'a') as f:
    words = database.execute("select ill from ANNALLWORD")
    words = database.fetchall()
    print("Start Make Dict")
    for x in trange(0, len(words)):
        word = (words[x])[0]
        f.write(word+'\n')

print("Finish Make dict")
