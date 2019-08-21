### Exercise 1:
# Print -20 to and including 50. Use any loop you want.

for idx in range(-20, 51, 1):
    print(idx)


### Exercise 2:
# Create a loop that prints even numbers from 0 to and including 20.
# Hint: You can find multiples of 2 with (whatever_number % 2 == 0)
for ndx in range(0, 22, 2):
    print(ndx)

### Exercise 3:
# Prompt the user for 3 numbers.
# Then print the 3 numbers along with their average after the 3rd number is entered.
# Refer to example below replacing ```NUMBER1```, ```NUMBER2```, ```NUMBER3```, and ```THEAVERAGE```
# with the actual values.
#
# Ex.Output
# ```
# The average of NUMBER1, NUMBER2, and NUMBER3 is THEAVERAGE
# ```
userInput1 = int(input("Enter 1st numb "))
userInput2 = input("Enter 2nd numb ")
userInput3 = input("Enter 3rd numb ")
print(userInput1,"+", userInput2,"+", userInput3, "=",
(userInput1+int(userInput2)+int(userInput3)))
