def main():
    """
    Temple Run: Curse of the Golden Idol
    You just grabbed a cursed golden idol from an ancient jungle temple, and the
    guardian spirit that protects it has woken up and is chasing you. Every choice
    you make from here decides whether you escape with the treasure, escape with
    nothing, or don't escape at all.
    """
    start()


def start():
    print("\nYou sprint through the crumbling temple corridor, torchlight flickering")
    print("behind you as the guardian spirit's roar echoes closer and closer.")
    print("Ahead, the path splits into three routes.\n")

    choice = input(
        "Do you go LEFT across the old rope bridge, RIGHT into the dark mine cart "
        "tunnel, or JUMP across the collapsing gap? "
    ).strip().upper()

    if choice == "LEFT":
        left()
    elif choice == "RIGHT":
        right()
    elif choice == "JUMP":
        jump()
    else:
        print("\nYou freeze, unsure which way to go, and the guardian catches up to you.")
        start()


def left():
    print("\n[Rope Bridge scenario coming soon...]")


def right():
    print("\n[Mine Cart Tunnel scenario coming soon...]")


def jump():
    print("\n[Collapsing Gap scenario coming soon...]")


if __name__ == "__main__":
    main()