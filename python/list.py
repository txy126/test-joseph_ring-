import time
import faker as fk
from memory_profiler import profile


class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


def create_people(total_numbers):
    people = []
    for i in range(total_numbers):
        fake = fk.Faker()
        name = fake.name()
        age = fake.random_int(min=1, max=100)
        gender = fake.random_element(elements=('male', 'female'))
        print(name, age, gender)
        people.append(Person(name, age, gender))
    return people


class JosephRing:
    def __init__(self, start, interval, people):
        self.start = start
        self.interval = interval
        self.people = people

    @profile
    def kill(self):
        index = start-1
        count = 0
        while len(people) > 1:
            if count == interval:
                people.pop(index)
                index -= 1
                count = 0
            index = (index+1) % len(people)
            count += 1
        return people[0]


start = int(input("start:"))
interval = int(input("interval:"))
total_numbers = int(input("total_numbers:"))

people = create_people(total_numbers)
joseph_ring1 = JosephRing(start, interval, people)

start_time = time.time()
winner = joseph_ring1.kill()
end_time = time.time()
print(f"the last person is {winner.name}")


print(f"cost time {end_time - start_time} seconds")

