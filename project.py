# Mysterious Forest Adventure
# A simple text-based choose-your-own-adventure game

print("=====================================")
print("   WELCOME TO THE MYSTERIOUS FOREST")
print("=====================================")
print()


def get_choice(valid_choices):
    """
    Keeps asking the player for input until they type
    something that matches one of the valid choices.
    Works no matter if they type UPPER, lower, or MiXeD case.
    """
    while True:
        answer = input("> ").upper()  # turn whatever they typed into CAPS
        if answer in valid_choices:
            return answer
        else:
            print("Hmm, that's not one of the options. Try again!")
            print("(Choices: " + ", ".join(valid_choices) + ")")


# ---------------------------------------------------------
# LEVEL 1 - The starting scenario (THREE choices here)
# ---------------------------------------------------------
def level_1():
    print("You wake up lost in a dark, misty forest.")
    print("Ahead of you, the path splits three ways.")
    print()
    print("GO LEFT")
    print("GO RIGHT")
    print("CLIMB TREE")
    print()

    choice = get_choice(["GO LEFT", "GO RIGHT", "CLIMB TREE"])

    if choice == "GO LEFT":
        level_2_river()
    elif choice == "GO RIGHT":
        level_2_cave()
    elif choice == "CLIMB TREE":
        level_2_village()


# ---------------------------------------------------------
# LEVEL 2 - Three different branches, each with its own choices
# ---------------------------------------------------------
def level_2_river():
    print()
    print("You walk left and find a wide, rushing river.")
    print("A rope bridge sways dangerously above it.")
    print()
    print("SWIM ACROSS")
    print("USE BRIDGE")
    print()

    choice = get_choice(["SWIM ACROSS", "USE BRIDGE"])

    if choice == "SWIM ACROSS":
        level_3_river_ending()
    elif choice == "USE BRIDGE":
        level_3_bridge_ending()


def level_2_cave():
    print()
    print("You walk right and discover the mouth of a dark cave.")
    print("A cold wind blows out from inside.")
    print()
    print("ENTER CAVE")
    print("WALK AWAY")
    print()

    choice = get_choice(["ENTER CAVE", "WALK AWAY"])

    if choice == "ENTER CAVE":
        level_3_cave_ending()
    elif choice == "WALK AWAY":
        level_3_walkaway_ending()


def level_2_village():
    print()
    print("You climb the tree and spot a tiny hidden village nearby!")
    print("Smoke rises from a chimney. Someone might be home.")
    print()
    print("KNOCK ON DOOR")
    print("SNEAK AROUND")
    print()

    choice = get_choice(["KNOCK ON DOOR", "SNEAK AROUND"])

    if choice == "KNOCK ON DOOR":
        level_3_villager_ending()
    elif choice == "SNEAK AROUND":
        level_3_sneak_ending()


# ---------------------------------------------------------
# LEVEL 3 - The endings. Every path leads somewhere different!
# ---------------------------------------------------------
def level_3_river_ending():
    print()
    print("The current is too strong! You are swept downstream")
    print("and wash up on a sunny, unfamiliar shore. Adventure awaits!")
    print("*** ENDING: THE DRIFTER ***")


def level_3_bridge_ending():
    print()
    print("The bridge creaks but holds! You cross safely and")
    print("find an old treasure chest hidden in the reeds.")
    print("*** ENDING: THE TREASURE FINDER ***")


def level_3_cave_ending():
    print()
    print("Deep in the cave, glowing crystals light your way.")
    print("You've discovered a secret underground kingdom!")
    print("*** ENDING: THE EXPLORER ***")


def level_3_walkaway_ending():
    print()
    print("You decide caves are creepy and head back to the forest,")
    print("where you build a cozy little camp and rest for the night.")
    print("*** ENDING: THE SURVIVOR ***")


def level_3_villager_ending():
    print()
    print("A kind old woman answers the door, feeds you a warm meal,")
    print("and tells you the safe way out of the forest.")
    print("*** ENDING: THE GUEST ***")


def level_3_sneak_ending():
    print()
    print("You sneak past unseen, but a dog starts barking loudly!")
    print("You run off into the trees, heart pounding with excitement.")
    print("*** ENDING: THE SNEAK ***")


# ---------------------------------------------------------
# Start the game!
# ---------------------------------------------------------
level_1()

print()
print("=====================================")
print("            THANKS FOR PLAYING")
print("=====================================")