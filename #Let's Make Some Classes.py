#Let's Make Some Classes

class Video_Game:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

people = {"Tom": 24, "Dick": 25, "Harry": 26}
#for name, age in people.items():
 #   print(f"My name is {name} and my age is {age} years old.")


def average_even_numbers(numbers):
    even_sum = 0
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_sum += n 
            even_numbers.append(n)   
    return even_sum / len(even_numbers)


students = {
    "Alice": 90,
    "Bob": 75,
    "Charlie": 82,
    "Diana": 65
}



honor_students = {}

for student, grade in students.items():
    if grade >= 80:
        honor_students[student] = grade + 5
        #honor_students.update({student : grade + 5}) same damn thing

print(honor_students)