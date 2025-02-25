# import logging
# logging.basicConfig(filename="checklogs.txt",format='%(asctime)s : %(levelname)s',level=40)
# def add(a,b):
#     try:
#         return a+b
#     except:
#         print("please enter int val only")
# add(2,5)
import logging

logging.basicConfig(filename="checklogs.txt", format='%(name)s : %(asctime)s : %(levelname)s : %(message)s ', level=logging.INFO)
logger=logging.getLogger("addition.py")
def add(a, b):
    try:
        c=int(a)+int(b)
        print(c)
        logger.info("programme run's ans = %s",c)
    except:
        logger.error("Invalid input: Only integers are allowed, given input = %s and %s",a,b)
        print("Please enter integer values only")

# add(2, 5)
