class LampHelper:
    def __init__(self):
        """Prints the welcome message when
            the game starts for the first time."""
        print("______________________________________________\n")
        print("Welcome to the Lamp Troubleshooting Game!")
        print("Type 'end' to exit.")
        print("______________________________________________")

    def play(self, plugged_in: str, light_bulb: str):

        if plugged_in[0].lower() == "y":
            if light_bulb[0].lower() == "y":
                print("Buy a new lamp!")
            else:
                print("Buy a new light bulb")
        else:
            print("Plug the lamp in!")

        print("________________\n")
        return "End!"
