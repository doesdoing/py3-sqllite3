import sqlite3


class SQL():
    def __init__(self):
        self._tables = ''
        self._path = ''
        self.target = ''
        self.vales = ''
        self._cmd = ''

    def TABLE(self, *args):
        self._tables = args[0]
        return self

    def PATH(self, *args):
        self._path = args[0]
        return self

    def DELETE(self, **args):
        if args:
            for x in args:
                self.target = x
                self.vales = args[x]
        if self.target and self.vales:
            self._cmd = 'DELETE FROM '+self._tables+' WHERE ' + \
                self.target+' = \'{}\''.format(self.vales)
        return self

    def FIND(self, **args):
        if args:
            for x in args:
                self.target = x
                self.vales=args[x]
        if self.target and self.vales:
            self._cmd = "select * from " + self._tables + ' where ' + \
                self.target+' like \'%{}%\''.format(self.vales)
        else:
            self._cmd = "select * from " + self._tables
        return self

    def ADD(self, **args):
        if args:
            self.target = []
            self.vales = []
            self.v = []
            for x in args:
                self.target.append(x)
                self.v.append('?')
                self.vales.append(args[x])
        if self.target and self.vales:
            self._cmd = "INSERT INTO "+self._tables + " ("+",".join(str(x) for x in self.target) + ") VALUES ("+",".join(str(x) for x in self.v) + ")"
        return self
    def UPDATE(self, **args):
        if args:
            self.target = []
            self.vales = []
            self.v = []
            for x in args:
                self.target.append(x)
                self.v.append(x+'=?')
                self.vales.append(args[x])
        return self
    def TARGET(self, **args):
        if self.target and self.vales:
            a=''
            for x in args:
                a=x+'='+args[x]
            self._cmd = "UPDATE "+self._tables+" SET " + ",".join(str(x) for x in self.v) + " where "+a
        return self
    def RUN(self):
        print(self._cmd)
        connect = sqlite3.connect(self._path)
        cursor = connect.cursor()
        if type(self.vales)==list:
            cursor.execute(self._cmd,self.vales)
        else:
            cursor.execute(self._cmd)
        res = cursor.fetchall()
        cursor.close()
        connect.commit()
        connect.close()
        return res


