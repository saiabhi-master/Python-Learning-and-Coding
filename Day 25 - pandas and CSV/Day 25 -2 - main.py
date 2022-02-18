import pandas
import csv

data = pandas.read_csv("squirrels.csv")
grey_sq = data[data["Primary Fur Color"] == "Gray"]
cinna_sq = data[data["Primary Fur Color"] == "Cinnamon"]
black_sq = data[data["Primary Fur Color"] == "Black"]
print(len(grey_sq))
print(len(cinna_sq))
print(len(black_sq))

data_dic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(grey_sq), len(cinna_sq), len(black_sq)]
}

data_fr = pandas.DataFrame(data_dic)
data_fr.to_csv("squirrelcount.csv")



# for line in fur_color:
#     x = 0
#     if line["Primary Fur Color"] == Gray:
#         x += 1
#
#     print(x)