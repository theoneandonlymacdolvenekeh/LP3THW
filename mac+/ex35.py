for sys import exit

def gold_room():
    print("This room is full og gold.  How much do you take?")
    
    choice = input("> ")
    if "O" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
        
    if how_much < 50:
        print("Nice, you're not greedy, you wih!")
        exit(0)
    else:
        dead("You greedy bastard!")
        
        

def bear_room():
    print("There is a bear here.")
    print("There bear has a bunch of honey.")
    print("the fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you theb slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved fron the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "tuant bear" and bear_moved:
            dead("The bear gets pissed off chews your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I go: no idea what that means.")
            

def cthulhu_room():
    print("Here you see the great evil cthulhu")
    print("He, it, whatever stares at you and you go insane.")
    print("Da you flee for your life or eat your head.")
    
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()
        
        
        
def dead(why):
    print(why, "Good job!")
    exit(0)
    
    
def start():
    print("You are in a dark room.")
    print("There is a door to right and left.")
    print("Which one do you take?")
    
    
    choice = input("> ")
    
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room():
    else:
        dead("You stumble around the room until you starve.")
        

start()    