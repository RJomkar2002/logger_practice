import logging
from addtion import add
from subtraction import sub

logging.basicConfig(filename="checklogs.txt", format='%(name)s : %(asctime)s : %(levelname)s : %(message)s ', level=logging.INFO)
logger=logging.getLogger("main.py")

def main():
    choice=int(input(" Add[1] \n Sub[2] \n enter choice for : "))
    if choice==1:
            num1=input("enter 1st num : ")
            num2=input("enter 2nd num : ")
            add(num1,num2)

    elif choice==2:
            num1 = input("enter 1st num : ")
            num2 = input("enter 2nd num : ")
            sub(num1, num2)

    else:
        logger.error("Invalid input enter valid choice")


if __name__=="__main__":
    main()



