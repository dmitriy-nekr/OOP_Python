class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def set_mark_for_unit(self, lecturer, course, mark):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.courses_marks :
                lecturer.courses_marks[course] += [mark]
            else:
                lecturer.courses_marks[course] = [mark]
        else:
            return 'Ошибка!'

    def average_grade(self):
        grades_for_courses = []
        for grades in list(self.grades.values()):
            middle_for_course = sum(grades)/len(grades)
            grades_for_courses.append(middle_for_course)
        average = sum(grades_for_courses)/len(grades_for_courses)
        return average

    def __str__(self):
        average = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{average}\nКурсы в процессе изучения:{",".join(self.courses_in_progress)}\nЗавершенные курсы:{",".join(self.finished_courses)}'

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_marks = {}


    def __str__(self):
        average = self.average_mark()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{average}'

    def average_mark(self):
        grades_for_courses = []
        for grades in list(self.courses_marks.values()):
            middle_for_course = sum(grades) / len(grades)
            grades_for_courses.append(middle_for_course)
        average = sum(grades_for_courses) / len(grades_for_courses)
        return average

    def __eq__(self, other):
        return self.average_mark() == other.average_mark()

    def __lt__(self, other):
        return self.average_mark() < other.average_mark()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student = Student('Ruoy', 'Eman','male')
student.courses_in_progress += ['Python', 'SQL']
student.finished_courses += ['Java', 'Git']


student2 = Student('Oleg', 'Gazmanov','male')
student2.courses_in_progress += ['Python', 'SQL']
student2.finished_courses += ['JavaScript', 'Git']

reviewer = Reviewer('Sergey', 'Ivanov')
reviewer.courses_attached += ['Python']
reviewer2 = Reviewer('Petr', 'Bochkarev')
reviewer2.courses_attached += ['SQL']

lector = Lecturer('Pavel', 'Mamaev')
lector.courses_attached += ['Python']
lector2 = Lecturer('Aleksei', 'Popov')
lector2.courses_attached += ['SQL']

reviewer.rate_hw(student, "Python", 10)
reviewer.rate_hw(student2, "Python", 5)
reviewer2.rate_hw(student, "SQL", 8)
reviewer2.rate_hw(student2, "SQL", 4)

student.set_mark_for_unit(lector,'Python',6)
student.set_mark_for_unit(lector2,'SQL',8)
student2.set_mark_for_unit(lector,'Python',9)
student2.set_mark_for_unit(lector2,'SQL',9)



print(student)
print(student2)
print(student2 < student)
print(reviewer)
print(reviewer2)
print(lector)
print(lector2)
print(lector < lector2)


students = [student, student2]
lectors = [lector, lector2]

def middle_grade_for_homework(some_object_list, course):
    temp_result =[]
    for object0 in some_object_list:
        if course in object0.courses_in_progress:
            result = sum(object0.grades[course])/len(object0.grades[course])
            temp_result.append(result)
    middle = sum(temp_result)/len(temp_result)
    return f'По курсу {course} средняя оценка за домашние задания {middle}'


def middle_grade_for_lecture(some_object_list, course):
    temp_result =[]
    for object1 in some_object_list:
        if course in object1.courses_attached:
            result = sum(object1.courses_marks[course])/len(object1.courses_marks[course])
            temp_result.append(result)
    middle = sum(temp_result)/len(temp_result)
    return f'По курсу {course} средняя оценка за лекцию {middle}'

print(middle_grade_for_homework(students, 'Python'))
print(middle_grade_for_lecture(lectors, 'SQL'))

