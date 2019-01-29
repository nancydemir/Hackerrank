class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
	self.idNumber = idNumber
    def printPerson(self):
	print("Name:", self.lastName + ",", self.firstName)
	print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #   Write your constructor here
    def __init__(self, firstName, lastName, idNumber,scores):
	self.firstName = firstName
	self.lastName = lastName
	self.idNumber = idNumber
	self.scores = []
	
    def calculate(self):
        average = sum(scores)/len(scores)
        if 0 < =average < 40:
            letterGrade = "T"
        if 40 <= average <= 55:
            letterGrade = "D"
        if 55 <= average < 70:
            letterGrade = "P"
        if 70 <= average < 80:
            letterGrade = "A"
        if 80 <= average < 90:
            letterGrade = "E"
        if 90 <= average <= 100:
            letterGrade = "O"
            return(letterGrade)
            
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #   Write your function hereclas

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
