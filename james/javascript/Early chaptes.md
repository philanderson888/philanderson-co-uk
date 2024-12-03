
# Programming

## JavaScript

- Getting Started
    
    ```jsx
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <script>
    
            var x = "Hello";
            var y = "John";
            var z = x + y;
            console.log(x)
            console.log (y)
            console.log (z)
            
            var message = ("Hello, " + "Dolly");
            console.log(message)
            var x = "hello";
            //alert(x + "John")
            console.log(x +  "John")
            console.log (`${x} John`)
    
            cost = "The cost: " + 59.80;   
            console.log(cost)
    
            var firstPart = "Hello, ";
            var secondPart = "Dolly!";
            var show = firstPart + secondPart;
            console.log()
        </script>
    </body>
    </html>
    ```
    
    ```jsx
    var x = 5
    console.log(`x is ${x}`);
    
    Notes
    
    %(modulus) is the remainder symbol
        
    var num = 10;
    var anotherNum = 1;
    var popularNumber = num + anotherNum;
    
    var leftOver = 10 % 3;
    
    6. Math expressions: Unfamiliar operators
    
    num++
    num--
    
    var num = 1;
    var newNum = num++;
    
    8.Concatenating text strings
    
    Combining 2 strings is called Concatenating
    "2" + "2" = 22 not 4
    
    var x = "Hello";
    var y = "John";
    var z = x + y;
    
    var first = "Hello ";
    var second = "Person";
    var third = Hello + Person;
    is incorrect
    
    var firstPart = "Hello, ";
    var secondPart = "Dolly!";
    var show = firstPart + secondPart;
    is correct
    ```
    

## Python

- Getting Started
    
    ```python
    """Assign the string "Ping!" to
    the variable the_machine_goes on
    line 5, then print it out on line 6!"""
    --------------------------------------------------
    ministry = "The Ministry of Silly Walks"
    
    print len(ministry)
    print ministry.upper()
    
    --------------------------------------------------
    
    """Declare and assign your variable on line 4,
    then call your method on line 5!"""
    
    pi = 3.14
    print str(pi)
    
    --------------------------------------------------
    
    print 'Welcome to the Pig Latin Translator!'
    
    # Start coding here!
    original = raw_input("Enter your name\n")
    
    print "You entered "+ original
    
    ---------------------------------------------------
    def cube(number):
      return number * number * number
    
    def by_three(number):
      if number % 3 == 0:
        return cube(number)
      else:
        return False
    ----------------------------------------------------
    from module import math
    ----------------------------------------------------
    import math
    print math.sqrt(25)
    ----------------------------------------------------
    import math # Imports the math module
    everything = dir(math) # Sets everything to a list of things from math
    print everything # Prints 'em all!
    ----------------------------------------------------
    def hotel_cost(nights):
      return 140 * nights
    
    def plane_ride_cost(city):
      if city == "Charlotte":
        return 183
      elif city == "Tampa":
        return 220
      elif city == "Pittsburgh":
        return 222
      elif city == "Los Angeles":
        return 475
    
    def rental_car_cost(days):
      cost = days * 40
      if days >= 7:
        cost -= 50
      elif days >= 3:
        cost -= 20
      return cost
    -----------------------------------------------------
    ```
    
     
    
- Developing
    
    
    ```python
    start_list = [5, 3, 1, 2, 4]
    square_list = []
    
    print "this is the start list"
    print start_list
    
    for number in start_list:
      square_list.append(number * number)
    print "\nthis is the squared list"
    print square_list
    
    print "\nthis is the sorted list"
    square_list.sort()
    
    print square_list
    
    -------------------------------------------------------------------
    ```
  