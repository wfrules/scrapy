import pymysql
class db:
    def __init__(self):
        self.conn = pymysql.connect(host="192.168.1.192",user="root",passwd="rootmlf",db="res",port=55000)
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
        return self.cursor.fetchone()
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
        return self.cursor.lastrowid
    def saveUnique(self, tab, obj, uniqueField):
        sSql = "select * from " + tab + "  where " + uniqueField + '=%s'
        arrRet = self.nativeQry(sSql, [obj[uniqueField]])
        if len(arrRet) == 0:
            obj['id'] = self.saveObj(tab, obj)
            return obj
        else:
            return arrRet[0]
gDb = db()