import json
import tkinter as tk
import urllib.request

from data import Data

window = tk.Tk()
SCREEN_WIDTH = 30
temp_text = tk.StringVar()
temp_field = tk.Label(textvariable=temp_text, fg='black', bg='green', height=5, width=SCREEN_WIDTH, font=50)
temp_field.pack()

city_field = tk.Entry(fg="black", bg="yellow", width=SCREEN_WIDTH)
city_field.pack()


def create_url(city):
    return f"{Data.BASE_URL}?{Data.CITY_KEY}={city}&{Data.APPID_KEY}={Data.APPID}&{Data.UNITS_KEY}={Data.UNITS}"


def get_temp_from_json(json_str):
    json_dict = json.loads(json_str)
    main = json_dict[Data.MAIN_KEY]
    return main[Data.TEMP_KEY]


def get_temp_from_weather_api():
    url = create_url(get_city())
    weather_json = urllib.request.urlopen(url).read().decode(Data.ENCODING)
    temp = get_temp_from_json(weather_json)
    temp_text.set(temp)


def get_city():
    return city_field.get()


button = tk.Button(text='Get temp', fg='black', bg='orange', width=SCREEN_WIDTH, command=get_temp_from_weather_api)
button.pack()

window.mainloop()
