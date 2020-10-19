# 使用pymysql代替mysqldb防止出现没有sqlclient的情况
import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库