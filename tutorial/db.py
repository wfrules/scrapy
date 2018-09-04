import pymysql
import json
import os
class db:
    def __init__(self):
        objConfigFile = open(os.getcwd() + "/cliconfig.json", encoding='utf-8')  # 设置以utf - 8 解码模式读取文件，encoding参数必须设置
        objSetting = json.load(objConfigFile)
        self.conn = pymysql.connect(host=objSetting['host'], user=objSetting['user'], passwd=objSetting['passwd'], db=objSetting['db'], port=objSetting['port'])
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