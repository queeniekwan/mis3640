class Course():
    ''' Represents a course in Babson College '''
    def __init__(self, id='', title='', instructors=[], credits=4, enrolled=0, capacity=0):
        ''' attributes of an object Course: id, title, instructors, credits, enrolled, capacity '''
        self.id = id
        self.title = title
        self.instructors = instructors
        self.credits = credits
        self.enrolled = enrolled
        self.capacity = capacity
    
    def __str__(self):
        ''' prints the course'''
        instructors = ', '.join(self.instructors)
        return f'{self.id}  {self.title}  {instructors}  {self.credits:.2f}  {self.enrolled}/{self.capacity}'
    
    def add_course(self, number_of_students=1):
        ''' increases the number of enrolled students of a course when new students join'''
        self.enrolled += number_of_students
    
    def drop_course(self, number_of_students=1):
        ''' decreases the number of enrolled students of a course when students drop'''
        self.enrolled -= number_of_students

    def change_instructor(self, old_instructor, new_instructor):
        ''' replaces an old instructor with a new instructor'''
        for i, name in enumerate(self.instructors):
            if name == old_instructor:
                self.instructors[i] = new_instructor
    
    def __or__(self, other):
        ''' advises student which course to take based on current enrollment situation'''
        if self.enrolled < self.capacity and other.enrolled < other.capacity:
            return f'You can take both courses! They both have available spots.'
        elif self.enrolled >= self.capacity and other.enrolled >= other.capacity:
            return f'Oh no, both courses are full. You should look for other courses'
        elif self.enrolled < self.capacity and other.enrolled >= other.capacity: 
            return f'You should take {self.title}! There is only {self.enrolled} enrolled students and there are {self.capacity} spots.'
        elif self.enrolled >= self.capacity and other.enrolled < other.capacity:
            return f'You should take {other.title}! There is only {other.enrolled} enrolled students and there are {other.capacity} spots.'

def main():
    mis = Course('MIS3640', 'Problem Solving & Software Design', ['Zhi Li'], 4, 20, 20)
    mac_tom = Course('SME2000', 'Managerial Accounting and Operations', ['Richard Block', 'Bojan Amovic'], 6, 40, 40)
    print(mis)
    print(mac_tom)

    # print(mis | mac_tom)
    # mis.drop_course(2)
    # print(mis | mac_tom)
    # mac_tom.drop_course()
    # print(mis | mac_tom)
    # mis.add_course()
    # print(mis)

    # mac_tom.change_instructor('Richard Block', 'Richard Goulding')
    # print(mac_tom)

if __name__ == "__main__":
    main()
