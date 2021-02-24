#!/usr/bin/env python3

print("""You walk on a path with either left, right, or middle path..
        Do you walk on the left path or right path or do you choose the middle path?""")

path = input("-> ")

# == Left Path logic =======================
if path == "left":

    print("You stumble upon a plate of pancakes.")
    print("What do you do?\n")

    print("1. Eat the pancakes")
    print("2. Leave the pancakes")

    # == Pancake logic ============================
    pancakes = input("-> ")

    if pancakes == "1":
        print("1) You eat the pancakes. You are now full.")
    elif pancakes == "2":
        print("2) You leave the pancakes. You are now hungry.")
    else:
        print(f"N)Well, doing {pancakes} is probably better.")
        print("The Pancakes are left there.")

# == Right Path Logic =====================
elif path == "right":
    print("You stumble on a crack in the path. What do you do?\n")

    print("1. Step on the crack.")
    print("2. Jump over the crack.")
    print("3. Contemplate why your even thinking this far into it.")

    # == Crack Logic ======================
    crack = input("-> ")

    if crack == "1":
        print("1) You decide to step on the crack. You get a call from your mother that she broke her back.")
    elif crack == "2":
        print("2) You decide to jump over the crack. You avoid a call from your mother about a broken back!")
    else:
        print("N) The insanity rots your eyes into a pool of muck.")
        print("N) Good job!")

# == Middle Path Logic =====================
elif path == "middle":
    print("You see a castle in the distance. What do you do?\n")

    print("1. Head into the castle.")
    print("2. Go around the castle.")
    print("3. Sit down and eat a sandwich.")

    # == Castle Logic ======================
    castle = input("-> ")

    if castle == "1":
        print("You decided to go into the castle. You die from a witch.")
    elif castle == "2":
        print("You decided to go around the castle. Now the witch cannot hurt you.")
    else:
        print("You have decided to eat the sandwich. But at what cost?")
else:
    print("You did not select a path??? Good Call :)")
