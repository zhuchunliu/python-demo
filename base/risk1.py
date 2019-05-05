import pymysql

class risk:
    def find(self):
        db=pymysql.connect("localhost","root","123456","test")
        cursor=db.cursor()

        # try:
        #     cursor.execute("insert into teacher(name,age) values('%s','%s') "%("test123","23"));
        #     db.commit();
        # except:
        #     print("except:")
        #     db.rollback();

        cursor.execute("select * from teacher")
        print("num: ",cursor.rowcount)

        result=cursor.fetchall()

        for x in result:
            print("id:{},name:{},age:{}".format(x[0],x[1],x[2]))

        # 已经fetchall之后，想fetchone，必须要重新查询才可以
        cursor.execute("select * from teacher")
        print(cursor.fetchone())



        db.close()

risk().find();