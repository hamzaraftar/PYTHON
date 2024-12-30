
import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# # print(data["temp"])

data_dic = data.to_dict()
# print(data_dic)

temp_data = data["temp"].to_list()
# print(temp_data)

avg = sum(temp_data) / len(temp_data )
# print(avg)

print(data["temp"].mean())
print(data["temp"].max())