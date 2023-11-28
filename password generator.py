import random

valid_char="abcdefghijklmnopqrstuvwxys0123456789"
while True:
    if len==0:
        break
    len=int(input("please enter the lenght of the password you want:"))
    password="".join(random.sample(valid_char,len))
    print(password)
