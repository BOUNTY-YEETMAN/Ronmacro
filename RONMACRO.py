import autoit
from pynput import keyboard
import time
import webbrowser

print('Rise of nations country choosing macro developed by s13 =)')
print('----------------------------------------------------------')
print('Version 1.00')
print('Press F4 in order to activate the macro!')
print('WARNING: I am not responsible for any damage my script can cause, you must have roblox rise of nations open!')
print('---------------------------------------------------------------------------------------------------------')

def PickCountry(country):
    autoit.mouse_move(285, 625, speed=2)
    time.sleep(0.1)
    autoit.mouse_click("left", 285, 625)
    autoit.send(country)
    autoit.mouse_move(291, 657, speed=2)
    autoit.mouse_click('left', 291, 657)
    autoit.mouse_move(679, 964, speed=2)
    time.sleep(0.01)
    autoit.mouse_click('left', 679, 964)

    # Open a web browser and navigate to the specified URL
    webbrowser.open("https://www.youtube.com/channel/UCnF_wc9jWRRJCdFLa-9W5sg")

def germany():
    try:
        autoit.mouse_click(1009, 863)
    except Exception as e:
        print("Error in germany():", e)


    

def on_press(key):
    if key == keyboard.Key.f3:
        print(autoit.mouse_get_pos())
    elif key == keyboard.Key.f4:
        PickCountry(country)

country = input("Enter your country's name (NEEDS TO BE SPELT EXACTLY!): ")

if country.lower() == 'usa':
    country = 'United States'

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
# Germany Flag Location: 1009, 863
# Play Button Location: 1018, 959