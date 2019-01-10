def castle_room():
    print("game over")
def choice_room():
    print(""" 
    You are sudden hit by a entence and godly light.
    then with no worning it is consumed by the black.
    feet, body, hands, head, eyes, mind all was black. 
    in what semmed like the longest second, small, soft, lights  flicked illuminated the black room.
    two foating orbs apear in fornt of you. on the right, blind and red "leave room"
    on the left, dull, "choice"
    
    
    
    a soft voice wispers "your choice to make"
    """)
    
    choice = input("> ")
    trry = True
    
    trry = choice_leave_or_stay(choice, trry)
        
    while trry == False:
        print("your choice to make")
        choice = input("> ")
        trry = choice_leave_or_stay(choice, trry)
        
def choice_leave_or_stay(choice, trry):
    if(choice == "leave room"):

        castle_room()

    elif(choice == "choice"):
        
        choice_room_man()

    elif not choice == "leave room" or not choice == "choice":
        return False

def choice_room_man():
    
        
    print("""
    the walls begin to callapes ligh, matter and mind all fold.
    compersing in on its self 
    a burst of particles, matter begins to take shape
    you body forms and the your mind
    
    a kirby shaped man appearse. 
    the wisper you heard shapes form
                              _
                           _ooOoo_
                          o8888888o
                          88" . "88
                          (| -_- |)
                          O\  =  /O
                       ____/`---'\____
                     .'  \|\|     |//  `.
                    /  \|\|||  :  |||//  \
                   /  _||||| -:- |||||_  \
                   |   | \|\  -  /'| |   |
                   | \_|  `\`---'//  |_/ |
                   \  .-\__ `-. -'__/-.  /
                 ___`. .'  /--.--\  `. .'___
              ."" '<  `.___\_<|>_/___.' _> /"".
             | | :  `- \`. ;`. _/; .'/ /  .' ; |
             \  \ `-.   \_\_`. _.'_/_/  -' _.' /
   ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
    
    """)
    print('" yes or no are you a jurney man", he ask')
    
    
    
    choice2 = input("> ")
    if(choice2 == "leave room"):

        castle_room()
    
    elif(choice2 == "yes"):
        print("yes, you say.")
        
        bomb_room()
        
    elif(choice2 == "no"):
        print("no, you say.")  
        
        bomb_room()
        
        
    elif not choice2 == "yes" or not choice2 == "no":
        print("i am a man of yes or no")
        print(f'but you a man of words say "{choice2}"')
        print("okay")
        print("""
        the room begims to spin.
        fast and faster it goes
        you are floating with mysteriuos man
        
        he screams "IM KILASKHIS FATHER OF THE ELDER GOOS, SAGE OF INFINATE PATHS, YOU HAVE NADE YOUR CHOICE"
        """)
        rital_room()
        
    
    
    
    
    
    
    
choice_room()    
