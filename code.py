class Student:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
        self.listOfHours = []
        self.totOfHours = 0
        self.mark2 = 0
        self.lOg = []
        self.qualityPoint = 0
        self.GPA = 0
        self.dict = {'A':4, 'A-': 3.7,
                     'B+':3.7 , 'B':3, 'B-':2.7,
                     'C+':2.7, 'C':2,'C-':1.7,
                     'D+':1.3, 'D':1}
        self.nummark = 0
        self.totMark = []
    def getSurname(self):
        
        return self.surname
     
    def getName(self):
        
        return self.name
     
    def addGrade(self, mark, creditHours):
        a = self.dict.get(mark)
 #       print(a)
        self.nummark = a
        grade = [mark,creditHours]
        self.mark2 = creditHours * self.nummark
        self.listOfHours.append(creditHours)
        self.lOg.append(self.mark2)
        self.totMark.append(grade)
        return grade
    def getGrades(self):
        return self.totMark
     
    def getHours(self):

        float(self.totOfHours)
        self.totOfHours = sum(self.listOfHours)
        if self.totOfHours > 0 :
            return self.totOfHours
        else:
            return 0.0
       
    def getQPoints(self):
        float(self.qualityPoint)
        self.qualityPoint = sum(self.lOg)
        return float(self.qualityPoint)
     
    def getGPA(self):
        if self.qualityPoint > 0 and self.totOfHours > 0:
            self.GPA = float(self.qualityPoint) / float(self.totOfHours)
            return float(self.GPA)
        else:
            self.GPA = 0
            return None
    def __str__(self):
        return "{}, {}: {}; GPA: {}".format(self.surname, self.name, str(self.totMark), str(self.GPA))

##stud1 = Student("john", "brown")
##stud2 = Student("mary", "watson")
##print(stud1.getName())
##print(stud2.getSurname())
##stud1.addGrade("B",15.0)
##stud1.addGrade("D+",10.0)
##print(stud1.getGrades())
##print(stud2.getGrades())
##stlhours = stud1.getHours()
##stlQpts = stud1.getQPoints()
##print(stlhours, stlQpts)
##print(stud1.getGPA())
##print(stud2.getHours())
##print(stud2.getQPoints())
##print(stud2.getGPA())
##print(stud1)
##print(stud2)

# ############### TESTING of PART A ###########################
#
#        Code                       Expected Output                    
#
stud1 = Student("John", "Brown")
stud2 = Student("Mary", "Watson")
print(stud1.getName())              # John
print(stud2.getSurname())	    # Watson 
stud1.addGrade("B",15.0)
stud1.addGrade("D+",10.0)
print(stud1.getGrades())	     # [(‘B’, 15.0), (‘D+’,10.0)]
print(stud2.getGrades())            # []
st1hours = stud1.getHours()
st1Qpts = stud1.getQPoints()
print(st1hours, st1Qpts)	     # 25.0  58.0
print(stud1.getGPA())	            # 2.32
print(stud2.getHours())	            # 0.0
print(stud2.getQPoints())	    # 0.0 
print(stud2.getGPA())              # None
print(stud1)	                    # Brown, John: [(‘B’,15.0),(‘D+’,10.0)]; GPA: 2.32
print(stud2)                        # Watson, Mary: []; GPA: None 

 
