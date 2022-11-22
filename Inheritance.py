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
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        total = 0
        for score in self.scores:
            total += score
        average = total / len(self.scores)
        if average < 40:
            return "T"
        elif average < 55:
            return "D"
        elif average < 70:
            return "P"
        elif average < 80:
            return "A"
        elif average < 90:
            return "E"
        elif average <= 100:
            return "O"


s = Student("Heraldo", "Memelli", 8135627, [100, 80])
s.printPerson()
print("Grade:", s.calculate())