# ===== TEMPLE RUN 2: ESCAPE THE DEMON MONKEY =====

print("You're sprinting through the jungle temple, the ground crumbling behind you.")
print("A giant demon monkey is chasing you, and the path ahead splits into three directions.")
print()
print("What do you do?")
print("JUMP - Jump over the gap to the left path")
print("SLIDE - Slide under the fallen log on the right path")
print("DASH - Run straight through the middle, dodging obstacles")

choice1 = input("Enter your choice: ").upper()

# LEVEL 1: JUMP PATH
if choice1 == "JUMP":
    print()
    print("You leap across the gap and land on a shaky rope bridge!")
    print("The bridge is swaying, and you see two options ahead.")
    print("GRAB - Grab the vine hanging above you")
    print("RUN - Keep running across the bridge")

    choice2 = input("Enter your choice: ").upper()

    if choice2 == "GRAB":
        print()
        print("You swing off the bridge just as it collapses, landing safely on solid ground!")
        print("You escaped with a pouch of golden coins. YOU WIN!")
    elif choice2 == "RUN":
        print()
        print("You keep sprinting, but the bridge snaps beneath your feet!")
        print("You fall into the river below and wash up far from the temple. GAME OVER.")
    else:
        print()
        print("You freeze on the bridge, unsure what to do, and it collapses under you. GAME OVER.")

# LEVEL 1: SLIDE PATH
elif choice1 == "SLIDE":
    print()
    print("You slide under the log and land in a torch-lit tunnel.")
    print("You hear rushing water ahead and see a fork in the tunnel.")
    print("LEFT - Head toward the sound of water")
    print("RIGHT - Head toward a faint light")

    choice2 = input("Enter your choice: ").upper()

    if choice2 == "LEFT":
        print()
        print("You find an underground river and ride the current out of the temple!")
        print("You escape with a rare gem. YOU WIN!")
    elif choice2 == "RIGHT":
        print()
        print("You follow the light and end up trapped in a dead-end room.")
        print("The demon monkey catches up to you. GAME OVER.")
    else:
        print()
        print("You stand still, confused, and the tunnel collapses around you. GAME OVER.")

#LEVEL 1: DASH PATH
elif choice1 == "DASH":
    print()
    print("You dash through the middle, dodging swinging blades and spike traps.")
    print("You reach a giant stone door with strange symbols and see two levers.")
    print("PULL - Pull the left lever")
    print("PUSH - Push the right lever")

    choice2 = input("Enter your choice: ").upper()

    if choice2 == "PULL":
        print()
        print("The door creaks open, revealing a hidden staircase to the exit. YOU WIN!")
    elif choice2 == "PUSH":
        print()
        print("Spikes shoot out from the walls! You narrowly dodge them, but the monkey grabs you. GAME OVER.")
    else:
        print()
        print("You hesitate too long, and the door slams shut, trapping you inside. GAME OVER.")

# ---------- INVALID INPUT FOR LEVEL 1 ----------
else:
    print()
    print("You freeze, unsure which way to go, and the monkey catches up to you. GAME OVER.")