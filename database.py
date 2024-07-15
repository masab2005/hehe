import pymysql
import os
my_secret = os.environ['database_password']
timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mysql-1cae1465-muhammad-0221.i.aivencloud.com",
  password=my_secret,
  read_timeout=timeout,
  port=11450,
  user="avnadmin",
  write_timeout=timeout,
)
def load_info(username,password):
   result = connection.cursor()
   result.execute('SELECT * FROM info WHERE username = %s AND password = %s', (username, password, ))
   info = result.fetchone()
   return info

