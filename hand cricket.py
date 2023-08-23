# odd or even (yes ik its cringe)
import random as r

def bat(t : int):    
    print("====================BAT=======================")
    out = False
    runs = 0
    
    if t == None:
        while not out:
            cc = r.choice([0, 1, 2, 3, 4, 5, 6])
            pc = int(input("Enter your number: "))
            if pc >= 0 and pc <= 6:
                if pc != cc:
                    runs += pc
                    print("Computer choice: ", cc)
                    print("Runs: ", runs)
                else:
                    print("Computer choice: ", cc)
                    print("Out!")
                    print("\nRUNS: ", runs)
                    out = True
                    break
            else:
                print("Don't mess with me mf")
    else:
        target = t + 1
        while not out:
            cc = r.choice([0, 1, 2, 3, 4, 5, 6])
            pc = int(input("Enter your number: "))
            if pc >= 0 and pc <= 6:
                if pc != cc:
                    runs += pc
                    print("Computer choice: ", cc)
                    print("Runs: ", runs)
                else:
                    print("Computer choice: ", cc)
                    print("Out!")
                    print("\nRUNS: ", runs)
                    out = True
                if runs >= target and not out:
                    print("You win!")
                    break
                elif runs <= target and out:
                    print("I win!")
                    break
                elif runs <= target and not out:
                    pass
            else:
                print("Don't mess with me mf")

    return runs

def bowl(t : int):
    print("====================BOWL=======================")
    out = False
    runs = 0
    if t != None:
        target = t + 1
        while not out:
            cc = r.choice([0, 1, 2, 3, 4, 5, 6])
            pc = int(input("Enter your number: "))
            if pc <= 6 and pc >= 0:
                if pc == cc:
                    print("I'm out! ")
                    print("\nRUNS: ", runs)
                    out = True
                else:
                    runs += cc
                    print("Computer choice: ", cc)
                    print("Runs: ", runs)
                if runs >= target and not out:
                    print("I win!")
                    break
                elif runs <= target and out:
                    print("You win!")
                    break
                elif runs <= target and not out:
                    pass
                
            else:
                print("Don't mess with me mf")
    else:
        while not out:
            cc = r.choice([0, 1, 2, 3, 4, 5, 6])
            pc = int(input("Enter your number: "))
            if pc <= 6 and pc >= 0:
                if pc == cc:
                    print("I'm out! ")
                    print("\nRUNS: ", runs)
                    out = True
                else:
                    runs += cc
                    print("Computer choice: ", cc)
                    print("Runs: ", runs)
            else:
                print("Don't mess with me mf")
    return runs 
        


def toss():
    choice = input("Odd or even: ")
    cc = r.choice([0, 1, 2, 3, 4, 5, 6])
    pc = int(input("Enter your number: "))
    if choice == 'e' and (cc + pc) % 2 == 0:
        print("Computer choice: ", cc)
        c = input("You win! What would you like to do: ")
        if c == 'bat':
            x = bat(None)
            bowl(x)
        else:
            x = bowl(None)
            bat(x)
    else:
        c = r.choice(['bat', 'bowl'])
        print("I won! I choose to ", c)
        if c == 'bat':
            x = bowl(None)
            bat(x)
        else:
            x = bat(None)
            bowl(x)


toss()
