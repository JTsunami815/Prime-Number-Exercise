#Write your code below this line 👇

#creating a function that make sure that it is a prime number
def prime_checker(number):
  #start off a variable that says that the number is a prime number
  prime_num = True

  #set a for loop to see if the given number is a prime number.  If it is not, it will change the stated variable to False
  for i in range(2,number):
    #if the number divided by all the numbers ranging from 2 to the (number-1) result with no remainder, than it is not a prime number
    if number % i == 0:
      prime_num = False

  #if the prime_num is False, then it will print out "It's not a prime number."
  if prime_num == False:
    print("It's not a prime number.")
  #if the prime_num is true, then it will print out "It's is a prime number."
  else:
    print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



