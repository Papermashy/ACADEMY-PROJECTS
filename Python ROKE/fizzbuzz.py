def advanced_fizzbuzz():
    for i in range (1,106):
        current = ""
        if i % 3 == 0:
            current += "Fizz"
        if i % 5 == 0:
            current += "Buzz"
        if i % 7 == 0:
            current += "Meow" 
        if len(current) == 0:
            current = i
        print (current)        
 
def fizzbuzz ():
    for i in range (1,100):
        if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
           print("FizzBuzzMeow")
          
        elif i % 3 == 0 and i % 5 == 0:
           print("FizzBuzz")
          
        elif i % 3 == 0 and i % 7 == 0:
           print("FizzMeow")
          
        elif i % 5 == 0 and i % 7 == 0:
           print("BuzzMeow")
      
        elif i % 3 == 0:
            print("Fizz")
               
        elif i % 5 == 0:
            print ("Buzz")
           
        elif i % 7 == 0:
            print ("Meow")
               
        else: print (i)
          
advanced_fizzbuzz()
