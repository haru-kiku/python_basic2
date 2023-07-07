#  3都道府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています｡
weather_information = [
    {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
    {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
    {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
    {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
    {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
    {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
    {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
    {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
]
print(len(weather_information))

total_temp = 0.0
for weather in weather_information:
    total_temp = total_temp + weather["temperature"]

print(total_temp / len(weather_information))

oosaka_station = ""
for station in weather_information:
    if station["prefecture"] == "大阪府" and len(oosaka_station) > 0:
        oosaka_station = oosaka_station + "," + station["station"]
    elif station["prefecture"] == "大阪府":
        oosaka_station = oosaka_station + station["station"]

print(oosaka_station)

fukuoka_temp = 0.0
count = 0
for weather in weather_information:
    if weather["prefecture"] == "福岡県":
        fukuoka_temp = fukuoka_temp + weather["temperature"]
        count = count + 1
        
print(fukuoka_temp / count)
