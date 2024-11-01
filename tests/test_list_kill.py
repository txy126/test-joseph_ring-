import faker as fk
import unittest


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
    def kill(self):
        index = self.start-1
        count = 0
        while len(self.people) > 1:
            if count == self.interval:
                self.people.pop(index)
                index -= 1
                count = 0
            index = (index+1) % len(self.people)
            count += 1
        return self.people[0]

    
class TestJosephus(unittest.TestCase):
    def test_kill(self):


        people=create_people(3)
        joseph_ring1 = JosephRing(1, 2, people)
        expected_result = people[0].name

        winner = joseph_ring1.kill()
        actual_result = winner.name
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()

