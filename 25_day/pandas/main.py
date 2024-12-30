
import pandas
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # # print(data["temp"])

# data_dic = data.to_dict()
# # print(data_dic)

# temp_data = data["temp"].to_list()
# # print(temp_data)

# avg = sum(temp_data) / len(temp_data )
# # print(avg)

# print(data["temp"].mean())
# print(data["temp"].max())

data = pandas.read_csv("Central_Park.csv")
gray_squairral_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squairral_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squairral_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squairral_count)
# print(red_squairral_count)
# print(black_squairral_count)


data_dic = {
    "Fur Color":["Gray" , "Cinnamon" , "Black"],
    "Count":[gray_squairral_count , red_squairral_count , black_squairral_count ]
}
df = pandas.DataFrame(data_dic)
df.to_csv("squairral_count.csv")