from student import Student

def transformData(data):
	return Student(data[1], data[2], data[3],data[4])

def enterData():
	return input('Enter data seperated by comma: ').split(',')

def printListStudents(students):
	if len(students):
		for student in students:
			st = transformData(student)
			st.getStudentInfor()
	else:
  		print('No data')
