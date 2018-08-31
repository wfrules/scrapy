import pymysql
class db:
    def __init__(self):
        self.conn = pymysql.connect("localhost","root","root","vods")
        self.cursor = self.conn.cursor()
    def nativeQry(self, sql, params):#查询语法
        self.cursor.execute(sql, params)
        arrResult = []
        index = self.cursor.description
        for res in self.cursor.fetchall():
            row = {}
            for i in range(len(index)):
                row[index[i][0]] = res[i]
            arrResult.append(row)

        return arrResult
    def nativeExec(self, sql, params):#执行语法
        self.cursor.execute(sql, params)
    def commit(self):#提交任务
        self.conn.commit()
    def saveObj(self, tab, obj):
        listFields = []
        listSymbol = []
        listVal = []
        for key in dict(obj):
            if key not in ['images','image_urls']:
                listFields.append(key)
                listSymbol.append('%s')
                listVal.append(obj[key])
        sSql = "insert " + tab + "(" + ','.join(listFields) + ")values(" + ','.join(listSymbol) + ")"
        self.nativeExec(sSql, listVal)
        # self.nativeExec(sSql,tuple(listVal))
gDb = db()