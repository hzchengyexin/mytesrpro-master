from pymysql import cursors,connect
#连接数据库
conn = connect(host='127.0.0.1',user='root',password='cyx19940118',db='guest',charset='utf8mb4',cursorclass=cursors.DictCursor)
try:
	with conn.cursor() as cursor:
		sql = 'INSERT INTO sign_guest(realname,phone,email,sign,event_id,create_time) VALUES ("tom",15757166414,"tom@email.com",0,1,NOW());'
		cursor.execute(sql)
	conn.commit()

	with conn.cursor() as cursor:
		sql = 'SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s'
		cursor.execute(sql,('15757166414',))
		result = sursor.fetchone()
		print(result)
	finally:
		conn.Close()