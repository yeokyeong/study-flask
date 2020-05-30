import pymysql



def db_connector(sql):
    # Open database connection
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='mariadb', db='schema', charset='utf8',
                     autocommit=True)
    # Connection 으로부터 Cursor 생성  // cursor는 Fetch 동작을 관리
    cur =db.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    db.commit()
    return str(rows)



#  execute() 메서드를 사용하여 SQL 문장을 DB 서버에 보냄
# sql = "select * from user"
# cursor.execute(sql)

# fetchall(), fetchone(), fetchmany() 등의 메서드를 사용하여 데이타를 서버로부터 가져온 후, Fetch 된 데이타를 사용
# rows = cursor.fetchall()
# INSERT/UPDATE/DELETE 후 Connection 객체의 commit() 메서드를 사용하여 데이타를 확정 갱신

# print(rows)

# disconnect from server
# db.close()
