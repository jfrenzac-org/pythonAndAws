from class_1.class_examples.lamp_helper import LampHelper

# input()
# = --> Asignación
# == --> Comparación
# if  ==== "si"
# elif === "sino"
# else === "entonces"
# print()
# lower()

# Este código dice si debo o no comprar una lámpara nueva

"""
if ---> Si
elif ---> sino si
else ---> sino

"""

lamp_game = LampHelper()

while True:
    plugged_in = input("Is the lamp plugged in? ---> Y/N: ")

    if plugged_in[0].lower() not in ["e", "y", "n"]:
        print("This game only allows 'Yes' or 'No' answers")
        break

    if plugged_in[0].lower() == "e":
        print("Exiting program...")
        break

    light_bulb = input("Is the light bulb working? ---> Y/N: ")

    lamp_game.play(plugged_in, light_bulb)
