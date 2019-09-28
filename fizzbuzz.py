def fizzbuzz():
    output = []
    for number in range (1, 101):
        if number % 15 == 0:
            output.append('Fizzbuzz')
        elif number % 3 == 0:
            output.append('Fizz')
        elif number % 5 == 0:
            output.append('Buzz')
        else:
            output.append(number)
            
    return output

#print(fizzbuzz())

#1. create a method called fizzbuzz
#2. create an output array called output
#3. iterate from 1 to 100, each number is called number
    #3a. if NUMBER is a multiple of 3, append "FIZZ" to output
    #3b.  if NUMBER is multiple of 5, append "BUZZ" to output
    #3c. if NUMBER is multiple of 3 and 5, append "FIZZBUZZ" to output
    #3d. otherwise append NUMBER
#4. return OUTPUT