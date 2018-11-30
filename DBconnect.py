import pymysql.cursors
#connection = pymysql.connect(host = 'localhost',
#                             user = 'root',
#                             port = 3306,
#                             password = '')
#try:
#    with connection.cursor() as cursor:
#        cursor.execute('CREATE DATABASE library')
#finally:
#    connection.close()
#


#connection = pymysql.connect(host = 'localhost',
#                             user = 'root',
#                             port = 3306,
#                             password = '',
#                             db = 'library',
#                             cursorclass= pymysql.cursors.DictCursor)
#
#try:
#    with connection.cursor() as cursor:
#        sqlQuery = "CREATE TABLE IF NOT EXISTS copy(ISBN13 TINYTEXT, Copy TINYTEXT, ReturnDate TINYTEXT, BorrowID TINYTEXT, ReserveID TINYTEXT)"
#        cursor.execute(sqlQuery)
#finally:
#    connection.close()


connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             port = 3306,
                             password = '',
                             db = 'library',
                             cursorclass= pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sqlQuery = "SELECT copy FROM copy WHERE ISBN13= %s AND BorrowID IS NULL"
        cursor.execute(sqlQuery,('9780345476722'))
        result = cursor.fetchall()
        print result
finally:
    connection.close()