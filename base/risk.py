#! /usr/bin/python
'''
    按照新的风控等级，批量迁移数据
'''



import mysql.connector

class teac:
    def sel(self):

        mybd = mysql.connector.connect(host="localhost",user="root",passwd="123456",database="test")
        mycursor = mybd.cursor()

        # 修改数据，需要commit
        # mycursor.execute("insert into teacher(name,age) values(%s,%s) ",params=("jack","23"))
        # mybd.commit();
        #
        mycursor.execute("select * from teacher")
        result=mycursor.fetchall()

        for x in result:
            print("id:{},name:{},age:{}".format(x[0],x[1].decode('utf-8'),x[2]))

        # 已经fetchall之后，想fetchone，必须要重新查询才可以
        mycursor.execute("select * from teacher")
        resultone = mycursor.fetchone()
        print(resultone)

teac().sel()


# class risk:
#     def __init__(url,database,username,pwd):
#         print(url)
#
#
# risk()