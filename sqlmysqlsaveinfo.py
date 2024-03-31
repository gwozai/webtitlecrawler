import pymysql

def singleton(cls):
    _instances = {}
    def _singleton(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return _singleton

@singleton
class DatabaseManager:
    def __init__(self, host, username, password, dbname):

        self.host = host
        self.user = username
        self.password = password
        self.db_name = dbname
        self.conn = None
        self.cursor = None

    def connect(self):
        # 创建数据库连接
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password)
        self.cursor = self.conn.cursor()

        # 检查数据库是否存在，如果不存在则创建数据库
        self.cursor.execute(f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{self.db_name}'")
        if self.cursor.fetchone()[0] == 1:
            self.cursor.execute(f"USE {self.db_name}")
        else:
            self.cursor.execute(f"CREATE DATABASE {self.db_name}")
            self.cursor.execute(f"USE {self.db_name}")

        # 创建表
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS webpage_info("
            "id INT AUTO_INCREMENT PRIMARY KEY,"
            "website_url VARCHAR(255),"
            "title VARCHAR(255),"
            "h1_titles TEXT,"
            "distinct_link_domains TEXT,"
            "screenshot_path VARCHAR(255),"
            "minio_path VARCHAR(255))"
        )

    def save_to_database(self, data):
        try:
            # 插入数据
            self.cursor.execute(
                "INSERT INTO webpage_info (website_url, title, h1_titles, distinct_link_domains, screenshot_path, minio_path) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    data['website_url'],
                    data['title'],
                    str(data['h1_titles']),
                    str(data['distinct_link_domains']),
                    data['screenshot_path'],
                    data['minio_path']
                )
            )

            # 提交事务
            self.conn.commit()

            return True
        except pymysql.Error as e:
            print(f"Error occurred: {e}")
            return False

    def close(self):
        # 关闭游标和连接
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()