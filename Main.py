from utils.Return import*
from utils.mangalist import*
import utils.dt as dt
from utils.borrow import*

class Main:
    def __init__(self):
        while(True):
            print("------------------------------------------------------")
            print("        Welcome to the Manga Management System     ")
            print("------------------------------------------------------")
            print("Enter 1. To Display Mangas")
            print("Enter 2. To Borrow Manga")
            print("Enter 3. To Return Manga")
            print("Enter 4. To Exit")
            try:
                a=int(input("Select a choice from 1-4: "))
                print()
                if(a==1):
                    with open("stock.txt","r") as f:
                        lines=f.read()
                        print(lines)
                        print ()
    
                elif(a==2):
                    Manga_list.mangalist()
                    Borrow.borrowManga()
                elif(a==3):
                    Manga_list.mangalist()
                    Return_manga.returnManga()
                elif(a==4):
                    print("Thank you for using Manga Management System")
                    exit()
                else:
                    print("Please enter a valid choice from 1-4")
            except ValueError:
                print("Please input as suggested.")

if __name__ == "__main__":
    Main()
