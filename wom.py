import random

fierce_dog = '''
               ------
             /  o    \         / / ~
 //\/\/\/\/\/   \/\/\/   ____/\ *  #
 /              /\/\/\        \ \ ~ 
 ____________________/
 L   L     L L 
 '''
  
baby_dog =  ''' 
      ____
     / .  \ 
 /\/\|   vv
 _______ ^^       
 L L L L
 
 
 '''
 
print "Hello and welcome to the World of Mathayas!"
name = raw_input( "What is your name?\n" )
print "Hello ",name,"!"
age = raw_input( "How old are you?\n" )
print age
print "I see. Well, I hope you are brave enough for my challenges!"
print "My name is The Math Master."
points = 39
has_wooden_sword = True
has_metal_sword = False
has_had_bonus_point = False
how_long_since_dog_came = 0
while True:
    print "You currently have ",points," points!"
    if has_wooden_sword:
        print "You also have a wooden sword!"
    if has_metal_sword:
        print "You also have a metal sword!"
    if points > 14 and not has_wooden_sword:
        if raw_input( "You have done well. Would you like a wooden sword? It costs 4 points." ) == "yes":
            print "OK! Great! Have a wooden sword!"
            has_wooden_sword = True
            points = points - 4
    if points > 16 and how_long_since_dog_came > 20:
        how_long_since_dog_came = 0
        print fierce_dog
        print "The dog of doom has come to eat your points!"
        if has_wooden_sword or has_metal_sword:
            print "You fight the dog with your sword. He runs away. Well done!"
            if not has_had_bonus_point:
                print "You get a bonus point!"
                points = points + 1
                has_had_bonus_point = True
        else:
            print "You run away. The dog eats two of your points."
            points = points - 2
    if points > 40 and not has_metal_sword:
        if raw_input( "You have done very well. Would you like a metal sword? It costs 20 points." ) == "yes":
            print "OK! Great! Have a metal sword!"
            has_metal_sword = True
            points = points - 20
    a = random.randint(3,9)
    b = random.randint(3,9)
    how_long_since_dog_came = how_long_since_dog_came + 1
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
