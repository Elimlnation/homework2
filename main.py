# Exercise 1
import os

file_path = r'C:\Users\cereg\PycharmProjects\homework2\requirements.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    print(content)
else:
    print('File not found')
# Exercise 2
# from faker import Faker
#
# fake = Faker()
#
# users = []
# for _ in range(100):
#     user = f'Name: {fake.name()}/ Email: {fake.email()}'
#     users.append(user)
#
# for user in users:
#     print(user)
# Exercise 3
# import csv
#
# file_path = r'C:\Users\cereg\PycharmProjects\homework2\hw.csv'
#
# heights = []
# weights = []
#
# with open(file_path, 'r') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     for row in csv_reader:
#         if len(row) >= 3:
#             heights.append(float(row[1]))
#             weights.append(float(row[2]))
#
# average_height = round(sum(heights) / len(heights), 3)
# average_weight = round(sum(weights) / len(weights), 3)
#
# print(f'Average Height: {average_height} cm')
# print(f'Average Weight: {average_weight} kg')
# Exercise 4
# import requests
#
# url = 'http://api.open-notify.org/astros.json'
# response = requests.get(url)
#
# data = response.json()
# number_of_astronauts = data['number']
#
# print(f'Number of astronauts currently in space: {number_of_astronauts}')