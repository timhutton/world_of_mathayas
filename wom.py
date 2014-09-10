import random

fierce_dog = '''
               ------
             /  o    \         / / ~
 //\/\/\/\/\/   \/\/\/   ____/\ *  #
 /              /\/\/\        \ \ ~ 
 ____________________/
 L   L     L L 
 '''
 
print fierce_dog

print "Hello and welcome to the World of Mathayas!"
name = raw_input( "What is your name?\n" )
print "Hello ",name,"!"
age = raw_input( "How old are you?\n" )
print age
print "I see. Well, I hope you are brave enough for my challenges!"
print "My name is The Math Master."
points = 7
while True:
    print "You currently have ",points," points!"
    a = random.randint(3,20)
    b = random.randint(3,20)
    while True:
        try:
            answer = int(raw_input( "What is "+str(a)+" + "+str(b)+" ?" ))
            if answer == a + b:
                print "Correct! Well done!"
                points = points + 1
                break
            else:
                print "I'm sorry, that wasn't the right answer."
                print "Please try again. Good luck!"
        except:
            print "Sorry?"

