import os
import sqlite3


class data(object):
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor


class database(object):

    def __init__(self, path, datasename):
        self.path = path
        self.datasename = datasename
        self.tempdata = data(None, None)

    def __creatdatabase__(self):
        try:
            databaseconn = sqlite3.connect(self.path + '/' + self.datasename)
            database = databaseconn.cursor()
        except:
            print("Creat Database failed")
            return False
        return data(databaseconn, database)

    def creat(self, tablename, tableinfo):
        # ?tableinfo is "id integer primery key others,class text..."
        self.tempdata = self.__creatdatabase__()
        databaseconn = self.tempdata.conn
        database = self.tempdata.cursor
        values = "(%s)" % tableinfo
        order = "creat table %s (%s)" % (tablename, values)
        try:
            database.execute(order)
        except:
            print("Creat table failed!")
        databaseconn.commit()

    def insert(self, tablename, values, ignore):
        # ? values = [[class,values],...]
        if self.tempdata.conn == None:
            print("No such a table!")
            return False

        tag = [x[0] for x in values]
        value = [x[1] for x in values]
        tag = "(%s)" % (','.join(tag))
        for x in range(0, len(value)):
            if type(value[x]) is str:
                value[x] = "\'%s'\'" % (value[x])
            else:
                value[x] = str(value[x])
        value = ','.join(value)

        if (ignore):
            order = "insert or ignore into %s (%s) values (%s)" % (
                tablename, tag, value)
        else:
            order = "insert into %s (%s) values (%s)" % (
                tablename, tag, value)

        try:
            dataconn = self.tempdata.conn
            database = self.tempdata.cursor
            database.execute(order)
            dataconn.commit()
        except:
            print("Insert Wrong!")

    def close(self):
        self.tempdata.conn.commit()
        self.tempdata.cursor.close()
        self.tempdata.conn.close()
