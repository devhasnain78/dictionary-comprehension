import random
students = ['Hasnain','Raza','mulli','papar']
student_score = {names: random.randint(1,100) for names in students}
# print(student_score)
passed_score = {name: score for (name,score) in student_score.items() if score>60}
print(passed_score)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
temp_c = {day: temp * 9/5 + 32 for (day,temp) in weather_c.items()}
print(temp_c)