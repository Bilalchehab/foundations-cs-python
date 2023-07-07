#1)
number = input("please enter a positive integer")
number = int(number)

while(number < 0):
  print("please enter a positive integer")
  number = input("please enter a positive integer")
  


def factorial(number):
  
  for x in range(number):
    if(number>0):
      print(x) 


  
  return 
    
    
print(factorial(number))


###########################################
##### QUESTION 2 
###########################################

number1 = input("please enter an integer")
number1 = int(number1)
list1 =[]

def function1():
  for i in range(number1) : 
    if(i>0 and number1%i == 0 ):
      print(i)
      list1.append(i)
  return
    
  
  
print(function1())

print(list1)




  
#############################################
####### QUESTION 3
#############################################

input1 = input("please enter your text here")

def reverseString():
  for i in range(len(input1)) :
    i = input1[i]
    print(i)
    
  return
  

# how can i make that it is only printed one time.
reverseString()



#######################################
#QUESTION4
########################################

  
my_list= []
new_list=[]
number_of_items = int(input("how many items do you want to enter"))
 
for i in range(number_of_items) :
    input2 = int(input("please enter your values here"))
    input2 = int(input2)
    my_list.append(input2)
    
print(my_list)
  
     

def myFunction3():
  for i in my_list :
    if i%2 == 0 : 
      print(i)
      new_list.append(i)
      
print(new_list)

myFunction3()






###########################
#Quetion5
###########################


password = input("Please enter a password")
special_character =("#","!","?","$")
number0 =("1", "2", "3", "4", "4", "5", "6", "7", "8", "9", "0")

def function5():
  if len(password) >= 8 :
    if any(x.isupper() for x in password):
      if any(x.lower() for x in password):
        if (x in number0 for x in password) :
          if (x in special_character for x in password) :
            print("strong password")
  else:
    print("weak password please try again")
    input("Please enter a password")
    if len(password) >= 8 :
      if any(x.isupper() for x in password):
        if any(x.lower() for x in password):
          if (x in number0 for x in password) :
            if (x in special_character for x in password) :
                print("strong password")
    

function5()



######################################
#Question5
######################################



            
          
  