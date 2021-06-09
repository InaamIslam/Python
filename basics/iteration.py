
#### A while loop will continue to execute a block of code while a condition is True.
#### If the condition is never True then the while loop will never start.

# number = 1
# while number < 5:
#     print(number)
#     number += 1

####+= this adds one to the variable preventing the loop from running infiintley
####so it will add one until the conditional becomes invalid and then moves onto next block of code
####This is because it is now invallid - doesnt fulfill condition 

####FOR LOOPS 

# people = ["Victoria", "John", "Rob", "James"]

# for person in people:
#         print(person)

#### most of the time people use i - to identify the variable

# people = ["Victoria", "John", "Rob", "James"]

# for i in people:
#         print(i)

#### Often ranges are used for For loops 

# for number in range(10):
#         print(number)

####with strings 

# for book_title in "This is the end of the show":
#         print(book_title)

#### ADDING BREAKS AND CONTINUE 

for number in range(10):
        print(number)
        if number == 7:
                break

for number in range(10):
        print(number)
        if number == 7:
                continue
      







