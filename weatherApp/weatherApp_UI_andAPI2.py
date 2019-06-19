##############################################################
# From youtube @ https://www.youtube.com/watch?v=D8-snVfekto
# How to Program a GUI Application (with Python Tkinter)!
# Good source for Doc is at:
#   https://www.tutorialspoint.com/python/python_gui_programming.htm
#
##############################################################

import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

# Intermediat test to ensure button functioning
def test_function(entry):
    print("This is the entry:", entry)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


##########################################################################
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
#0b83cf55b99bdb1a4e3154150e910864
##########################################################################
def get_weather(city):
    weather_key = '0b83cf55b99bdb1a4e3154150e910864'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
#    print out formatted weather from json response
#    print(weather['name'])
#    print(weather['weather'][0]['description'])
#    print(weather['main']['temp'])
      
    label['text'] = format_response(weather)
    
########################################################################
#print test before using API
########################################################################
#    print(response.json())
##########################################################################
#
# App goes here...

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font = ('Script', 40))
#Could do additional formatting of above...
#label = tk.Label(lower_frame, font = ('Script', 40), anchor='nw', justify='left', bd=4)

label.place(relwidth=1, relheight=1)

root.mainloop()
