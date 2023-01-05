import pandas

data=pandas.read_csv("weather-data.csv")
data_dict=data.to_dict()
#print(data_dict)
data_temp=data.temp
#temp_list=data_temp.to_list()
print(data_dict)
print(data_temp)
#print(data)
temp_max=data_temp.max()
temp_mean=data_temp.mean()
print(data[data.day=="Monday"])
print(data[data.temp==temp_max])

student_data={"Names":["Dare", "Segs", "Dad"], "Scores":[12,43,23]}
data=pandas.DataFrame(student_data)
print(data)

data.to_csv("SCORE BOARD.csv")