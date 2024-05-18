import autoit
from pynput import keyboard
import time
import webbrowser
import pyautogui
import random

print('Rise of nations country choosing macro developed by s13 =)')
print('---------------------------------------------------------------------------------------------------------')
print('Version 1.2')
print('Press F4 in order to activate the macro!')
print('WARNING: I am not responsible for any damage my script can cause, you must have roblox rise of nations open!')
print('---------------------------------------------------------------------------------------------------------')

country = input("Enter your country's name (NEEDS TO BE SPELT EXACTLY!): ")

def PickCountry(country):
    if country.lower() == 'germany':
        # Germany:
        autoit.mouse_click("left",1009, 863,speed=2)
        time.sleep(0.01)
        autoit.mouse_click("left",1018,959,speed=2)

    elif country.lower() == 'russia':
        # Russia:
        autoit.mouse_click("left",960, 832,speed=2)
        time.sleep(0.01)
        autoit.mouse_click("left",951, 962,speed=2)
    
    elif country.lower() == 'japan':
        autoit.mouse_click("left",911, 832,speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left',907, 961,speed=2)
    
    elif country.lower() == 'brazil':
        autoit.mouse_click('left',860, 832,speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left',853, 959,speed=2)
    elif country.lower() == 'south korea':
        autoit.mouse_click("left",1060, 866,speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left',1061, 959,speed=2)
    elif country.lower() == 'turkey':
        autoit.mouse_click("left",960, 864,speed=2)
        time.sleep(0.01)
        autoit.mouse_click("left",958, 959,speed=2)
    elif country.lower() == 'nigeria':
        autoit.mouse_click("left",911, 866,speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left',907, 959,speed=2)
    elif country.lower() == 'pakistan':
        autoit.mouse_click('Left',862, 865,speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left',854, 959,speed=2)
    elif country.lower() == 'indonesia':
        autoit.mouse_click("left",1012, 830,speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left',1063, 960,speed=2)
    elif country.lower() == 'mexico':
        autoit.mouse_click('left',1010, 831,speed=2)
        time.sleep(0.01)
        autoit.mouse_click('left',1010, 955,speed=2)
    else:
        # Other Countries:
        autoit.mouse_click('left',388, 627,speed=2)
        time.sleep(0.01)
        autoit.send(country)
        autoit.mouse_click('left', 381, 658,speed=2)
        autoit.mouse_click('left', 679, 964,speed=2)

    webbrowser.open("https://www.youtube.com/channel/UCnF_wc9jWRRJCdFLa-9W5sg")
    
def on_press(key):
    if key == keyboard.Key.f4:
        PickCountry(country)

democountries = {
    'japan',
    'brazil'
}

communistCountries = {
    'vietnam',
    'cuba',
    'china'
}

if country.lower() == 'usa':
    country='United States'
elif country.lower() == 'us':
    country='United States' 
elif country.lower()=='baguette':
    country='France'
elif country.lower()=='sk':
    country='South Korea'
elif country.lower()=='nk':
    country='North korea'
elif country.lower()=='indo':
    country='indonesia'
elif country.lower()=='fun':
    ideology=input('What ideoglogy? (democratic, communism, ): ')
    if ideology == 'democratic':
        question=input('Do you have USA unlocked? (Y/N): ')
        question2=input('Do you have india unlocked? (Y/N): ')
        if question.upper() == 'Y':
            democountries.add('USA')
        if question2.upper() == 'Y':
            democountries.add('India')
    democountries_list = list(democountries)
    randomcountry = random.choice(democountries_list)
    country=randomcountry
    

    if ideology == 'communist':
        questiondemo=input('Do you have china unlocked? (Y/N): ')
        if questiondemo.upper() == 'Y':
            communistCountries.add('china')
    communistCountries_list = list(communistCountries)
    randomcountry1 = random.choice(communistCountries_list)
    country=randomcountry1




listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
