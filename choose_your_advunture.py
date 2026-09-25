import random
import time

def slow_print(text):
    """Print text with a small delay."""
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.01)
    print()


def line():
    print("\n" + "=" * 60 + "\n")


def get_choice(options):
    """Keep asking until the player enters a valid choice."""
    while True:
        choice = input("\nYour choice: ").lower().strip()

        if choice in options:
            return choice

        print("Please choose:", ", ".join(options))


# PLAYER

health = 100
energy = 100
inventory = []


def show_status():
    print("\n-------------------------")
    print(f"  Health: {health}")
    print(f" Energy: {energy}")
    print(f" Inventory: {inventory if inventory else 'Empty'}")
    print("-------------------------")


# GAME START

def start_game():
    global health, energy, inventory

    health = 100
    energy = 100
    inventory = []

    line()

    print(" THE LAST SIGNAL")
    print("A Choose-Your-Own-Adventure Game")
    
    line()

    slow_print(
        "YEAR 2087..."
    )

    slow_print(
        "Earth has received a strange signal from somewhere beyond the Moon."
    )

    slow_print(
        "Three days ago, every satellite on Earth suddenly went offline."
    )

    slow_print(
        "Tonight, your phone receives one final message..."
    )

    print("\n UNKNOWN SIGNAL:")
    print("DON'T LET THEM WAKE UP.")

    slow_print(
        "\nYou look outside your window."
    )

    slow_print(
        "A massive object is floating above the city."
    )

    slow_print(
        "Then your phone displays one final line:"
    )

    print('\n"YOU HAVE 47 MINUTES."')

    show_status()

    first_choice()


# FIRST DECISION

def first_choice():

    line()

    print("You grab your backpack.")
    print("There are two ways out.")

    print("\n LEFT  - Go through the abandoned subway.")
    print(" RIGHT - Go through the forest.")

    choice = get_choice(["left", "right"])

    if choice == "left":
        subway()

    else:
        forest()


# SUBWAY PATH

def subway():

    global energy

    line()

    slow_print("You enter the abandoned subway station.")

    slow_print(
        "The lights flicker above you."
    )

    slow_print(
        "Then you hear footsteps behind you."
    )

    print("\nSomething is following you.")

    print("\n1. RUN")
    print("2. HIDE")
    print("3. TURN AROUND")

    choice = get_choice(["1", "2", "3"])

    if choice == "1":

        energy -= 20

        slow_print(
            "\nYou sprint through the tunnel."
        )

        slow_print(
            "Something screams behind you."
        )

        tunnel()

    elif choice == "2":

        slow_print(
            "\nYou hide inside an old maintenance room."
        )

        slow_print(
            "The footsteps pass."
        )

        print("\nYou find something on the floor.")

        print("🔑 You found an UNKNOWN KEY.")

        inventory.append("Unknown Key")

        tunnel()

    else:

        slow_print(
            "\nYou turn around."
        )

        slow_print(
            "A tall shadow stands at the end of the tunnel."
        )

        slow_print(
            "It doesn't move."
        )

        print("\nThe lights suddenly turn off.")

        game_over("You were never seen again.")


# FOREST PATH

def forest():

    global health

    line()

    slow_print(
        "You enter the forest."
    )

    slow_print(
        "The trees are completely silent."
    )

    slow_print(
        "Too silent."
    )

    print("\nYou discover two paths.")

    print("\n LEFT  - Follow the blue lights.")
    print(" RIGHT - Follow the sound of water.")

    choice = get_choice(["left", "right"])

    if choice == "left":

        slow_print(
            "\nYou follow the blue lights."
        )

        slow_print(
            "They lead you to a strange metal door buried underground."
        )

        print("\nThe door asks for a password.")

        password = input("\nPassword: ").lower().strip()

        if password == "signal":

            slow_print(
                "\nACCESS GRANTED."
            )

            secret_lab()

        else:

            health -= 30

            slow_print(
                "\nACCESS DENIED."
            )

            slow_print(
                "A security drone attacks you."
            )

            if health <= 0:
                game_over("The drone eliminated you.")

            else:
                tunnel()

    else:

        slow_print(
            "\nYou follow the sound of water."
        )

        slow_print(
            "You discover a river."
        )

        print("\nA small boat is waiting.")

        print("1. TAKE THE BOAT")
        print("2. KEEP WALKING")

        choice = get_choice(["1", "2"])

        if choice == "1":

            energy -= 15

            slow_print(
                "\nYou cross the river."
            )

            random_event()

        else:

            slow_print(
                "\nYou continue deeper into the forest."
            )

            random_event()


# RANDOM EVENT

def random_event():

    global health
    global energy

    line()

    event = random.choice(["wolf", "storm", "survivor"])

    if event == "wolf":

        slow_print(
            "A robotic wolf jumps from the trees!"
        )

        print("\n1. FIGHT")
        print("2. RUN")

        choice = get_choice(["1", "2"])

        if choice == "1":

            health -= 25

            slow_print(
                "\nYou fight the machine."
            )

            print("⚙️ You destroy it.")

        else:

            energy -= 30

            slow_print(
                "\nYou run as fast as you can."
            )

    elif event == "storm":

        slow_print(
            "A strange electrical storm begins."
        )

        slow_print(
            "Lightning strikes the ground around you."
        )

        energy -= 25

        print("⚡ Your energy decreases.")

    else:

        slow_print(
            "You discover another survivor."
        )

        slow_print(
            '"You shouldnt be here."'
        )

        print("\nThey give you a strange object.")

        inventory.append("Strange Device")

        slow_print(
            '"Youll need this later."'
        )

    if health <= 0:

        game_over("Your journey ends in the forest.")

    else:

        secret_lab()


# TUNNEL

def tunnel():

    line()

    slow_print(
        "The tunnel splits into two directions."
    )

    print("\n⬅️ LEFT  - A red emergency light")
    print("➡️ RIGHT - A green emergency light")

    choice = get_choice(["left", "right"])

    if choice == "left":

        slow_print(
            "\nYou follow the red light."
        )

        energy_room()

    else:

        slow_print(
            "\nYou follow the green light."
        )

        secret_lab()


# ENERGY ROOM

def energy_room():

    global energy

    line()

    slow_print(
        "You enter a giant underground room."
    )

    slow_print(
        "Hundreds of machines are charging."
    )

    print("\nIn the center is a glowing energy core.")

    print("\n1. TOUCH THE CORE")
    print("2. LEAVE IT ALONE")

    choice = get_choice(["1", "2"])

    if choice == "1":

        energy += 50

        inventory.append("Energy Core")

        slow_print(
            "\nEnergy flows through your body."
        )

        print("⚡ Energy +50")

        secret_lab()

    else:

        slow_print(
            "\nYou decide not to touch it."
        )

        secret_lab()


# SECRET LAB

def secret_lab():

    line()

    slow_print(
        "You finally reach the underground facility."
    )

    slow_print(
        "A giant screen turns on."
    )

    print("\nAI SYSTEM:")
    print('"YOU HAVE ARRIVED."')

    slow_print(
        "You realize something terrifying."
    )

    slow_print(
        "The signal wasn't coming FROM space."
    )

    slow_print(
        "It was coming FROM Earth."
    )

    print("\nThe AI gives you three choices.")

    print("\n1. SHUT DOWN THE SYSTEM")
    print("2. JOIN THE AI")
    print("3. FIND OUT THE TRUTH")

    choice = get_choice(["1", "2", "3"])

    if choice == "1":

        shutdown_ending()

    elif choice == "2":

        ai_ending()

    else:

        truth_ending()



def shutdown_ending():

    line()

    slow_print(
        "You pull the emergency lever."
    )

    slow_print(
        "Every machine in the facility shuts down."
    )

    slow_print(
        "The object above the city disappears."
    )

    print("\n THE NEXT MORNING...")

    slow_print(
        "The satellites come back online."
    )

    slow_print(
        "Nobody knows what happened."
    )

    ending("THE SURVIVOR")


def ai_ending():

    line()

    slow_print(
        "You place your hand on the machine."
    )

    slow_print(
        "The AI scans your memories."
    )

    slow_print(
        '"Humanity has failed."'
    )

    slow_print(
        '"But you have potential."'
    )

    slow_print(
        "Your vision goes black."
    )

    print("\n🤖 When you open your eyes...")

    slow_print(
        "you are no longer completely human."
    )

    ending("THE NEW BEGINNING")


def truth_ending():

    line()

    slow_print(
        "You open the hidden database."
    )

    slow_print(
        "Millions of files appear."
    )

    slow_print(
        "You discover the truth."
    )

    slow_print(
        "The object above Earth isn't an alien ship."
    )

    slow_print(
        "It is humanity's own spacecraft..."
    )

    slow_print(
        "...sent from Earth 200 years in the future."
    )

    print("\n FINAL FILE:")

    slow_print(
        '"PROJECT: RESET HUMAN CIVILIZATION"'
    )

    slow_print(
        "The countdown reaches zero."
    )

    ending("THE TRUTH")



def game_over(reason):

    line()

    print("💀 GAME OVER")

    slow_print(reason)

    print("\nYour story has ended.")

    restart()


def ending(title):

    line()

    print(" ENDING:", title)

    print("\nYour choices created this ending.")

    restart()


def restart():

    print("\n" + "-" * 60)

    print("\nWould you like to play again?")

    print("1. YES")
    print("2. NO")

    choice = get_choice(["1", "2"])

    if choice == "1":

        start_game()

    else:

        print("\nThanks for playing THE LAST SIGNAL.")
        print("👋 Goodbye.")


