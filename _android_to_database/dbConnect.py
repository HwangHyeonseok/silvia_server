# DB 연결 (mysql)
import pymysql

def dbcon():
    # mysql 연결
    conn = pymysql.connect(host='127.0.0.1', user='root', password='h96071212!', db='member', charset='utf8') 
    if conn.open: # DB 연결 여부 확인
        print('데이터베이스에 연결되었습니다.')
    return conn

def dbclose(conn):
    conn.close() # DB 연결 해제