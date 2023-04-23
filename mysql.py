import pymysql
# 数据库连接参数



db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '2003wzh0905',
    'database': 'students',
    'charset': 'utf8mb4'
}

# 连接数据库
db = pymysql.connect(
    host= 'localhost',
    port= 3306,
    user= 'root',
    password= '2003wzh0905',
    database= 'students',
    charset= 'utf8mb4'

)

cursor = db.cursor()

# 通过pycharm创建数据库

create_table_sql = """
create table if not exists students_data (
    id int(11) AUTO_INCREMENT PRIMARY KEY,
    banji varchar(10),
    name varchar(20) not null,
    age int(3),
    score int(4)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""
cursor.execute(create_table_sql)

class MySQL:
    """MySQL数据库操作类"""
    def __init__(self,host,port,user,password,db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None
        self.cur = None


    def connect(self):
        """连接数据库"""
        try:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db
            )
            self.cur = self.conn.cursor()
        except Exception as e:
            print(f"连接数据库失败: {e}")

    def close(self):
        """关闭数据库"""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def execute(self, sql, params=None, fetch_one=False):
        """执行SQL语句"""
        try:
            self.connect()
            self.cur.execute(sql, params)
            self.conn.commit()

            if fetch_one:
                result = self.cur.fetchone()
            else:
                result = self.cur.fetchall()

            return result
        except Exception as e:
            self.conn.rollback()
            print(f"执行SQL语句失败: {e}")
        finally:
            self.close()