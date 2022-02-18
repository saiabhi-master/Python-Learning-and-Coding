# with open("weather_data.csv") as Data_file:
#     listy = []
#     for i in Data_file:
#         listy.append(i)
# print(listy)

import csv

# with open("weather_data.csv") as Data_file:
#     data = csv.reader(Data_file)
#     Temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             x = int(row[1])
#             Temperatures.append(x)
#     print(Temperatures)



import pandas

# data = pandas.read_csv("weather_data.csv")
#Beautifully printed out

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].max())




# setting = data[data.day == "Monday"]
# print(setting)
# temp_in_c = int(setting.temp)
#
# def con_c_to_f(t):
#
#     x = (t * (9/5) + 32)
#     return x
#
# print(con_c_to_f(temp_in_c))



# x = data.temp.max()
# that_day = (data[data.temp == x])
# print(that_day.condition)



#creating a data frame from Scratch:
data_dict = {
    "students": ["Amy", "Abhi", "Angela"],
    "scores": [66, 99, 84]
}

numb = 0
data = pandas.DataFrame(data_dict)
data.to_csv("New_data.csv")

now = pandas.read_csv("New_data.csv")
print(now.scores[1])

