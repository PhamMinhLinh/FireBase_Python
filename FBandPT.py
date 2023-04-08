from firebase import firebase
import random as rd
import time

random_number1 = rd.randint(1, 10)
random_number2 = rd.randint(10,20)
firebase=firebase.FirebaseApplication("https://argon-radius-377619-default-rtdb.firebaseio.com/", None)

pk ="/room"
led1='/led1'
led2='/led2'

while True:
 random_number1 = rd.randint(1, 10)
 random_number2 = rd.randint(10, 20)
 result=firebase.put(pk,led1,random_number1)
 result=firebase.put(pk,led2,random_number2)
 time.sleep(5)