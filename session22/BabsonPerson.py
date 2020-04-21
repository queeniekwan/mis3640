from Person import Person


class BabsonPerson(Person):
    next_id = 0

    # next ID number to assign

    def __init__(self, name):
        # initialize Person attributes
        Person.__init__(self, name)
        # new BabsonPerson attribute: a unique ID number
        self.id = BabsonPerson.next_id
        BabsonPerson.next_id += 1

    # sorting Babson people uses their ID number, not name!
    def __lt__(self, other):
        return self.id < other.id

    def speak(self, utterance):
        return self.name + " says: " + utterance


def main():
    p1 = BabsonPerson('Zhi')
    p2 = BabsonPerson('Andrew')
    p3 = BabsonPerson('Steve')
    p4 = Person('Donald')

    print(p4.id)

    print(p2.speak("I feel good today"))

    print(p4.speak("I don't feel good today"))


if __name__ == "__main__":
    main()
