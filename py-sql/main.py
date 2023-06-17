import database
import util

mydb = database.connectDb()
cursor = mydb.cursor()

print('1. Get list students. \n')
print('2. Add new student. \n')
print('3. Edit student by code. \n')
print('4. Find student by code. \n')
print('5. Delete student by code. \n')

work = input('Enter your work: ')
print('\n')

if work == '1':
	students = database.getListStudents(cursor)
	util.printListStudents(students)

elif work == '2':
	studentData = util.enterData()
	database.addNewStudent(mydb, cursor, studentData)
	students = database.getListStudents(cursor)
	util.printListStudents(students)

elif work == '3':
	code = (input('Enter student code: '), )
	results = database.findStudents(cursor, code)

	if len(results):
		name, className = util.enterData()
		data = (name, className, code[0])
		database.updateStudents(mydb, cursor, data)
		students = database.getListStudents(cursor)
		util.printListStudents(students)
	else:
		print('No data')

elif work == '4':
	code = (input('Enter student code: '), )
	results = database.findStudents(cursor, code)
	util.printListStudents(results)

elif work == '5':
	code = (input('Enter student code: '), )
	database.deleteStudents(mydb, cursor, code)
	students = database.getListStudents(cursor)
	util.printListStudents(students)

else:
	print('Your work is invalid!')