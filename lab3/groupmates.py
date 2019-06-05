groupmates = [
    {
        "name": u"Михаил",
        "group": "17-01",
        "age": 19,
        "marks": [4, 4, 4, 4, 4]
    },
    {
        "name": u"Владимир",
        "group": "17-01",
        "age": 20,
        "marks": [5, 5, 5, 5, 5]
    },
    {
        "name": u"Константин",
        "group": "17-01",
        "age": 18,
        "marks": [3, 3, 4, 4, 4]
    },
    {
        "name": u"Василий",
        "group": "17-01",
        "age": 20,
        "marks": [5, 5, 4, 5, 4]
    },
    {
        "name": u"Данил",
        "group": "17-01",
        "age": 19,
        "marks": [5, 4, 3, 4, 4]
    }
]

print ("\n")

def print_students(students):
    print (u"Имя студента".ljust(15), \
          u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20))
    for student in students:
        print (student["name"].ljust(15), \
              student["group"].ljust(8), \
              str(student["age"]).ljust(8), \
              str(student["marks"]).ljust(20))
    print ("\n")

print_students(groupmates)
average = float(input("\n Введите среднюю оценку: "))
averageArray = []

def computeAverageMarks(students):
    temp = students["marks"]
    sum = 0
    for i in range(len(temp)):
        sum += temp[i]
    return sum/5

for i in range(len(groupmates)):
    j = 0
    if(computeAverageMarks(groupmates[i]) > average):
        averageArray.append(groupmates[i])
        j = j + 1

if(len(averageArray) == 0):
    print("\n" +  "Не существует студентов, чья средняя оценка больше чем " + str(average) + "!\n")
else:
    print ("\n" + "Студенты, чья средняя оценка выше чем " + str(average) + ": " + "\n")
    print_students(averageArray)


