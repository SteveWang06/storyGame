import random



HP = 100
Thirst = 100
Hunger = 100
turn = 50
step = 0
ran = 0
event_choice = 0
diffculty = 0

print("Welcome To Word RPG!!\nPress Enter key to start.\n")

def level():

    print('''
        (0) Monkey
        (1) Easy
        (2) Normal
        (3) Hard
        (4) Insane

    ''')
    while True:
        try:
            menu_value = int(input("menu_value is: "))

            if(menu_value == 0):
                Monkey()
                
                break
            elif(menu_value == 1):
                diffculty = 1
                Easy()
                
                break
            elif(menu_value == 2):
                diffculty = 2
                Normal()
                
                break
            elif(menu_value == 3):
                diffculty = 3
                Hard()
                
                break
            elif(menu_value == 4):
                diffculty = 4
                Insane()
                
                break
            else:
                print("Wrong input,please select level again!\n\n")
        except:
            print("Wrong input,please select level again!\n\n")


def menu():

    print('''What do you want to do?
        (0) Move left
        (1) Move right
        (2) Move forward
        (3) Check status
    ''')

    while True:
        
        menu = int(input("menu_value is: "))

        if(menu == 0):
            moveLeft()                
            break
        elif(menu == 1):           
            moveRight()                
            break
        elif(menu == 2):           
            moveForward()                
            break
        elif(menu == 3):            
            status()               
            break
            
def status():
    print("HP = %d\nThirst = %d\nHungry = %d\n", HP, Thirst, Hunger)
    menu()


def moveLeft():
    step = 0
    checklevel()
    step += 2
    if (step == 2):
        event2()

def moveRight():
    checklevel()

def moveForward():
    step = 0
    checklevel()
    step += 1
    if (step == 1):
        event1()
    


def Monkey():
    menu()

def Easy():
    menu()

def Normal():
    menu()

def Hard():
    menu()

def Insane():
    menu()

def event1():
    Thirst = 100
    Hunger = 100
    print("你是一名邊緣人，沒有人想理你，好可憐噢\n水-5\t食物-5\n")
    Thirst -= 5
    Hunger -= 5
    checkDeath()

def event2():
    HP = 100
    Thirst = 100
    Hunger = 100

    print("天己暗\n你打算在福星客棧借宿一宵\n沒想到與你同房的室友「GArY」邀請你\"共度良宵\"\n是否接受?\t(1 / 0)\n");
    event_choice = input('event_choice: ')
    if (event_choice == 1):
    
        random1()
        if (ran == 1):
        
            print("隱藏結局 : 知男而上\n恭喜通關!\n")
            exit(0)
        
        else:
        
            print("你度過了一個安詳的夜晚\nHP = 100\tThirst = 100\tHunger = 100\n")
            HP = 100
            Thirst = 100
            Hunger = 100
            menu()
           
    elif (event_choice == 0):
    
        print("你拒絕了GArY的好意\n孤單地過了一個寒冷的夜晚\nHP - 5\tThirst - 5\tHunger - 5")
        HP -= 5
        Thirst -= 5
        Hunger -= 5
        checkDeath()
    
#def event3():

def checklevel():
    Thirst = 100
    Hunger = 100
    if(diffculty == 0):
        return 0
    elif(diffculty == 1):
        Thirst = Thirst - 1
        Hunger = Hunger - 1
    elif(diffculty == 2):
        Thirst = Thirst - 2
        Hunger = Hunger - 2
    elif(diffculty == 3):
        Thirst = Thirst - 3
        Hunger = Hunger - 3
    elif(diffculty == 4):
        Thirst = Thirst - 4
        Hunger = Hunger - 4


def checkDeath():

    if (HP == 0 or Thirst == 0 or Hunger == 0):
    
        print("GAME OVER!")
        exit(0)
    
    else:
    
        menu()
    
def random1():
   
    ran = random() % 3 + 1



level()
menu()
    
    


