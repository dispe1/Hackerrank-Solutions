# Problem: https://www.hackerrank.com/challenges/30-inheritance/problem
# Difficulty : Easy
# Score : 30

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, score):
        self.person = Person(firstName, lastName, idNumber)
        self.score = sum(score) / len(score)
        if (90 <= self.score <= 100):
            self.grade = 'O'
        elif (80 <= self.score):
            self.grade = 'E'
        elif (70 <= self.score):
            self.grade = 'A'
        elif (55 <= self.score):
            self.grade = 'P'
        elif (40 <= self.score):
            self.grade = 'D'
        else:
            self.grade = 'T'


    def printPerson(self):
        self.person.printPerson()

    def calculate(self):
        return self.grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
