import faker as fk
import time
from memory_profiler import profile
from collections import deque


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
        dq = deque(self.people)
        count = start-2
        while len(dq) > 1:
            temp = dq.popleft()
            count += 1
            if count == interval:
                count = 0
                continue
            else:
                dq.append(temp)
        return dq[0]


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
