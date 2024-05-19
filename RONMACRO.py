import autoit
import time
import webbrowser
import random
import tkinter as tk
from pynput import keyboard

def PickCountry(country):
    country = country.lower()
    if country == 'germany':
        autoit.mouse_click("left", 1009, 863, speed=2)
        time.sleep(0.01)
        autoit.mouse_click("left", 1018, 959, speed=2)
    elif country == 'russia':
        autoit.mouse_click("left", 960, 832, speed=2)
        time.sleep(0.01)
        autoit.mouse_click("left", 951, 962, speed=2)
    elif country == 'japan':
        autoit.mouse_click("left", 911, 832, speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left', 907, 961, speed=2)
    elif country == 'brazil':
        autoit.mouse_click('left', 860, 832, speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left', 853, 959, speed=2)
    elif country == 'south korea':
        autoit.mouse_click("left", 1060, 866, speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left', 1061, 959, speed=2)
    elif country == 'turkey':
        autoit.mouse_click("left", 960, 864, speed=2)
        time.sleep(0.01)
        autoit.mouse_click("left", 958, 959, speed=2)
    elif country == 'nigeria':
        autoit.mouse_click("left", 911, 866, speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left', 907, 959, speed=2)
    elif country == 'pakistan':
        autoit.mouse_click('left', 862, 865, speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left', 854, 959, speed=2)
    elif country == 'indonesia':
        autoit.mouse_click("left", 1012, 830, speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left', 1063, 960, speed=2)
    elif country == 'mexico':
        autoit.mouse_click('left', 1010, 831, speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left', 1010, 955, speed=2)
    else:
        autoit.mouse_click('left', 388, 627, speed=2)
        time.sleep(0.01)
        autoit.send(country)
        autoit.mouse_click('left', 381, 658, speed=2)
        autoit.mouse_click('left', 679, 964, speed=2)

    webbrowser.open("https://www.youtube.com/channel/UCnF_wc9jWRRJCdFLa-9W5sg")

def on_press(key):
    if key == keyboard.Key.f4:
        PickCountry(country_var.get())

def start_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def handle_special_cases(country):
    if country.lower() == 'usa':
        return 'united states'
    elif country.lower() == 'us':
        return 'united states'
    elif country.lower() == 'baguette':
        return 'france'
    elif country.lower() == 'sk':
        return 'south korea'
    elif country.lower() == 'nk':
        return 'north korea'
    elif country.lower() == 'indo':
        return 'indonesia'
    elif country.lower() == 'random':
        webbrowser.open('https://random.country')
        return 'website Opened'
    elif country.lower() == 'uk':
        return 'united kingdom'
    elif country.lower() == 'hard':
        return 'cook islands'
    else:
        return country


def submit_country():
    country = handle_special_cases(country_var.get())
    if country.lower() == 'random':
        webbrowser.open('https://random.country')
    else:
        country_var.set(country)
        start_listener()

# Set up the tkinter GUI
root = tk.Tk()
root.title("Rise of Nations Country macro! V5.0")

tk.Label(root, text="Enter your country's name (NEEDS TO BE SPELT EXACTLY!):").pack()
country_var = tk.StringVar()
tk.Entry(root, textvariable=country_var).pack()

tk.Button(root, text="Submit", command=submit_country).pack()

# Informational Labels
tk.Label(root, text="Press F4 to activate the macro!").pack()
tk.Label(root, text="WARNING: I am not responsible for any damage my script can cause, you must have Roblox Rise of Nations open!").pack()

democountries = {'japan', 'brazil', 'United States'}
communistCountries = {'vietnam', 'cuba', 'china'}
DailyChallengeCountries = {'Cook islands', 'antartica', 'poland', 'mexico'}

root.mainloop()
