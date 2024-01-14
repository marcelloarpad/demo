import pymysql
class MySqlConOp(object):
    """
    mysql连接以及数据操作类
    """
    def __init__(self,host="localhost",user="root",password="root",database="mysql",port="3306"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.db = self.get_db()
        self.cur = self.get_cursor()

    def get_db(self):
        """
        连接数据库
        return:database
        """
        db = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             database=self.database,
                             port=self.port
                             )
        return db
    def get_cursor(self):
        """
        使用cursor方法获取操作游标
        return:cursor对象
        """
        db_cursor = self.db.cursor()
        return db_cursor
    def close_db(self):
        """
        关闭数据库连接
        return: 无
        """
        self.cur.close()
        self.db.close()

    def query_all(self,query_str):
        """
        根据条件查询所有记录
        param query_str-SQL语句
        return:results-查询结果集
        """
        try:
            cursor = self.get_cursor()
            #run sql statement
            cursor.execute(query_str)
            #获取所有记录
            results=cursor.fetchall()
            return results
        except Exception as ex:
            print("执行错误：{}",format(ex))
        finally:
            self.close_db()

    def query_one(self,query_str):
        """
        根据查询条件查询一条记录
        param：query_str-SQL语句
        return: results
        """
        try:
            cursor = self.get_cursor()
            #run sql statement
            cursor.execute(query_str)
            #获取一条记录
            results = cursor.fetchone()
            return results
        except Exception as  ex:
            print("执行错误；{}".format(ex))
        finally:
            self.close_db()

    def update_row(self,query_str):
        """
        根据更新语句更新数据记录
        param :query_str-SQL语句
        return: 无
        """
        try:
            cursor = self.get_cursor()
            #run sql statement
            cursor.execute(query_str)
            #提交到数据执行
            self.db.commit()
        except Exception as ex:
            print("执行错误；{}",format(ex))
            #发生错误回滚
            self.db.rollback()
        finally:
            self.close_db()

    #test class:MySqlConOp

    def pymysql_test(self):
        """
        数据查找
        """
        s_name ="李同学"
        sql = "select * from t_studentinfo where s_name='{}'".format(s_name)

        try:
            #创建数据库对象，获得连接对象和游标
            conn = MySqlConOp("localhost","root","root","mysql")

            results = conn.query_all(sql)
            #显示输出查询结果
            for row in results:
                num = row[0]
                name = row[1]
                birthday = row[2]
                address = row[3]
                print(f"学号={num},姓名={name},出生日期={birthday},家庭地址={address}")
        except:
            print("error:找不到数据")

    if __name__ == "__main__":
        pymysql_test()