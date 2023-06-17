class Student:
    def __init__(self,idSV,name,className,adress):
        self.id = idSV
        self.name = name
        self.className = className
        self.adress = adress
    
    def getIdSV(self):
        return self.idSV
    
    def getName(self):
        return self.name

    def getClassName(self):
        return self.className
    
    def getStudentInfor(self):
        print('Code: ' + self.idSV)
        print('Name: ' + self.name)
        print('Class: ' + self.className)
        print('Address: ' + self.address)
        print('-------------')