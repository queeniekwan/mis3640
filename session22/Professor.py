from BabsonPerson import BabsonPerson
from Person import Person

class Professor(BabsonPerson):
    def __init__(self, name, course):
        BabsonPerson.__init__(self, name)
        self.course = course

    def __str__(self):
        return Person.__str__(self) + ' ' + self.course
    
    def speak(self, something):
        new_utterance = 'In course ' + self.course + ' , we say ' + something
        return BabsonPerson.speak(self, new_utterance)

def main():
    faculty = Professor('Zhi Li', 'MIS 3640')
    print(faculty)
    print(faculty.speak('Python is cool!'))

if __name__ == "__main__":
    main()
