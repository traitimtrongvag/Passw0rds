import random
import string
import time as t
import threading
import os
def randstr1(length=10, include_special_chars=True):
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += "!@#$%^&*()_+-=[]{}.<>?~"
    return ''.join(random.choices(characters, k=length))
def randstr(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

stop_flag = False

def check_enter():
    global stop_flag
    input()  
    stop_flag = True
    
if __name__ == '__main__':
    
    
        print("""1 Random normal password
 2Random strong password
    """)
        choice = input()
        if choice == '1':
        
            threading.Thread(target=check_enter, daemon=True).start()

            i = 0
            print("Running")

            while not stop_flag:
                i += 1
                random_string = randstr(random.randint(7,12))
                print(f"{i} {random_string}")
                t.sleep(0.01)
    
  
            print(f"\nMật khẩu được chọn là: {random_string}")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '2':
            threading.Thread(target=check_enter, daemon=True).start()

            i = 0
            print("Running")

            while not stop_flag:
                i += 1
                random_string = randstr1(random.randint(7,12))
                print(f"{i} {random_string}")
                t.sleep(0.01)
    
  
            print(f"\nThe chosen password is: {random_string}")
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            
        else:
           print("Invalid input, press Enter to try again")
           input()  
           os.system('cls' if os.name == 'nt' else 'clear')
       
