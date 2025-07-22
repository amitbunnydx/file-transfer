# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {key:(value * 9/5) + 32 for key,value in weather_c.items()}
#
# print(weather_f)
import pandas

new_data={
    'days':["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"],
    'temp':[12,14,15,14,21,22,25]
}
df=pandas.DataFrame(new_data)
for index,data in df.iterrows():
    if data.temp==14:
        print(data.days)
