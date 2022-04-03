import pandas

# Data frame, 2 dimensional
data = pandas.read_csv("./day-25/weather_data.csv")

# Series, 1 dimensional
# print(data["temp"])
# Converts column titles to attributes
# e.g. data.temp (like obj) instead of data["temp"] (like dict)

# Dataframe from scratch:
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
data = pandas.DataFrame(data_dict)
print(data)

# high_temp = data.temp.max()
# print(data[data.temp == high_temp])
# She does data[data.temp == data.temp.max()]
# avoids storing data in variable

# monday = data[data.day == "Monday"]
# print(monday.temp * 1.8 + 32)


# print(data[data.day == "Monday"])

# Returns dictionary of csv
# data_dict = data.to_dict()

# Returns list of temp column
# temp_list = data["temp"].to_list()

# print(data["temp"].max())


# average = sum(temp_list) / len(temp_list)
# print(round(average))
# Can use data["temp"].mean() instead

# import csv

# with open("./day-25/weather_data.csv") as weather_history:
#     data = csv.reader(weather_history)
#     temperatures = []
#     for temps in data:
#         if len(temps[1]) <= 3:
#             temperatures.append(int(temps[1]))

# print(temperatures)
# # She uses if row[1] != "temp"
