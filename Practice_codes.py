# learnt : # printing , # string , # input , # variables #new line, #concatenation, #debugging, #spaces, #commenting

#Print string with concatenation with space
print("Hi"+" "+"Shreya" + "\nGood Night")

#Print string with concatenation without space
print("Hi "+"Shreya" + "\nGood Night")

#print
print("A")

#store in variable
a, b, c= 1, 2 ,3
print(a, b, c)

#input function
input('had your lunch?')
print (("hi shreya ") + (input ("had your lunch?")))

#length of name
human = "hello "
print(human)
print ((human) + input("what is name" ), (len(human)))
print(len(input("what is name" )))

#length of character with storing in variable
name = "shreya"
length=len(name)
print(length)

# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice.
# Write 3 lines of code to switch the contents of the variables. You are not allowed 
# to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.

glass1 = "milk"
glass2 = "juice"
temp = glass1
glass1=glass2
glass2 = temp
print("glass1 =", glass1 , "and glass2 =", glass2)


#band name generator project

print("Welcome to the Band name generator\n")
Place = input("Where are you from?\n")
Pet = input("Your pet name\n")
print("Place:",Place , "and Pet:", Pet)
print("Your Band name is: "+ Place+" "+Pet) #this is best 


  


