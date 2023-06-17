import mysql.connector
import constant

def connectDb():
	return mysql.connector.connect(
		host=constant.dbInfor["host"], 
		user=constant.dbInfor["user"], 
		passwd=constant.dbInfor["passwd"], 
		database=constant.dbInfor["database"]
	)

def getListStudents(cursor):
	cursor.execute("SELECT * FROM students")
	results = cursor.fetchall()
	return results if len(results) else []

def addNewStudent(mydb, cursor, data):
	sql = "INSERT INTO students (code, name, class) VALUES (%s, %s, %s)"
	cursor.execute(sql, data)
	mydb.commit()
	print(cursor.rowcount, "student inserted.")

def findStudents(cursor, code):
	sql = "SELECT * FROM students WHERE code = %s"
	cursor.execute(sql, code)
	results = cursor.fetchall()

	return results if len(results) else []

def updateStudents(mydb, cursor, data):
	sql = "UPDATE students SET name = %s, class = %s WHERE code = %s"
	cursor.execute(sql, data)
	mydb.commit()
	print(cursor.rowcount, "student(s) affected.")

def deleteStudents(mydb, cursor, code):
	sql = "DELETE FROM students WHERE code = %s"
	cursor.execute(sql, code)
	mydb.commit()
	print(cursor.rowcount, "student(s) deleted")
