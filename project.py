# Mysterious Forest Adventure
# My first text adventure game!

import random

# a few silly reactions the forest gives you when you type something invalid
# random.choice() just grabs one of these lines at random each time
oops_reactions = [
    "A confused squirrel drops an acorn on your head.",
    "Somewhere, an owl hoots as if laughing at you.",
    "The trees rustle, seeming to whisper, 'wrong answer!'",
    "A firefly blinks at you in disbelief.",
    "Your own echo repeats your mistake back at you."
]

print("=====================================")
print("   WELCOME TO THE MYSTERIOUS FOREST")
print("=====================================")

# ---------------------------------------
# LEVEL 1 - the start of the story
# This part has THREE choices instead of two
# ---------------------------------------

print("You wake up lost in a dark, misty forest.")
print("Your head is spinning, and you don't remember how you got here.")
print("Ahead of you, the path splits three ways.")
print()
print("GO LEFT")
print("GO RIGHT")
print("CLIMB TREE")
print()

choice1 = input("> ")
choice1 = choice1.upper()  

if choice1 == "GO LEFT":
    print()
    print("You hear the sound of rushing water pulling you leftward.")
    print("You walk left and find a wide, roaring river.")
    print("A rickety rope bridge sways dangerously above it.")
    print()
    print("SWIM ACROSS")
    print("USE BRIDGE")
    print()

    choice2 = input("> ")
    choice2 = choice2.upper()

    # LEVEL 3 - the ending
    if choice2 == "SWIM ACROSS":
        print()
        print("You take a deep breath and dive in!")
        print("The current is too strong! You are swept downstream")
        print("and wash up, gasping, on a sunny, unfamiliar shore.")
        print("A parrot squawks overhead, as if welcoming you home.")
        print("*** ENDING: THE DRIFTER ***  \U0001F30A")
    elif choice2 == "USE BRIDGE":
        print()
        print("Trying not to look down, you creep across plank by plank.")
        print("The bridge creaks but holds! Safely on the other side,")
        print("you spot an old treasure chest hidden in the reeds.")
        print("Inside: a rusty key and a map with a big red X.")
        print("*** ENDING: THE TREASURE FINDER ***  \U0001F5DD\uFE0F")
    else:
        print()
        print("You stand frozen at the riverbank, unsure what to do.")
        print(random.choice(oops_reactions))
        print("That is not a valid choice, so your adventure ends here.")
        print("(Hint: type SWIM ACROSS or USE BRIDGE next time!)")

elif choice1 == "GO RIGHT":
    print()
    print("A cold draft brushes past you, pulling you rightward.")
    print("You walk right and discover the mouth of a dark cave.")
    print("Strange whispers seem to echo from somewhere deep inside.")
    print()
    print("ENTER CAVE")
    print("WALK AWAY")
    print()

    choice2 = input("> ")
    choice2 = choice2.upper()

    # LEVEL 3 - the ending
    if choice2 == "ENTER CAVE":
        print()
        print("You light a torch and step into the darkness.")
        print("Deep in the cave, glowing crystals light your way,")
        print("revealing a secret underground kingdom of tiny miners!")
        print("They cheer and crown you their honorary guest.")
        print("*** ENDING: THE EXPLORER ***  \U0001F48E")
    elif choice2 == "WALK AWAY":
        print()
        print("You decide caves are far too creepy for your taste.")
        print("You head back to the forest and build a cozy little")
        print("campfire, roasting mystery berries under the stars.")
        print("*** ENDING: THE SURVIVOR ***  \U0001F525")
    else:
        print()
        print("You hesitate at the cave entrance, frozen with doubt.")
        print(random.choice(oops_reactions))
        print("That is not a valid choice, so your adventure ends here.")
        print("(Hint: type ENTER CAVE or WALK AWAY next time!)")

elif choice1 == "CLIMB TREE":
    print()
    print("Curiosity gets the better of you, and up you go!")
    print("From the treetop, you spot a tiny hidden village nearby.")
    print("Smoke curls from a chimney. Someone might be home.")
    print()
    print("KNOCK ON DOOR")
    print("SNEAK AROUND")
    print()

    choice2 = input("> ")
    choice2 = choice2.upper()

    # LEVEL 3 - the ending
    if choice2 == "KNOCK ON DOOR":
        print()
        print("Knock knock! A kind old woman answers, smiling warmly.")
        print("She feeds you a warm bowl of mushroom stew and points")
        print("you toward the safe path out of the forest.")
        print("*** ENDING: THE GUEST ***  \U0001F372")
    elif choice2 == "SNEAK AROUND":
        print()
        print("You tiptoe around the cottage, quiet as a mouse.")
        print("Suddenly a dog starts barking like crazy!")
        print("You bolt into the trees, heart pounding with excitement.")
        print("*** ENDING: THE SNEAK ***  \U0001F43E")
    else:
        print()
        print("You freeze on the village path, unsure what to do next.")
        print(random.choice(oops_reactions))
        print("That is not a valid choice, so your adventure ends here.")
        print("(Hint: type KNOCK ON DOOR or SNEAK AROUND next time!)")

else:
    print()
    print(random.choice(oops_reactions))
    print("That is not a valid choice, so your adventure ends here.")
    print("(Hint: type GO LEFT, GO RIGHT, or CLIMB TREE next time!)")

print()
print("=====================================")
print("            THANKS FOR PLAYING")
print("=====================================")