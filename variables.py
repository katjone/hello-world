
number_of_apples = 4

print("We have", number_of_apples, "apples.")

number_of_bananas = 7

print("We have", number_of_bananas, 'bananas.')

number_of_bananas += 2


print('we found some more bananas... now we have', number_of_bananas, 'bananas.')


people = 2

print('There are ', people, 'people in here!')

banana_share = number_of_bananas / people

apple_share = number_of_apples / people

print ("Each person gets", int(banana_share), 'bananas and', int(apple_share), 'apples.' )



## What types of variables do we know so far? 
## - integers   23
## - floats     0.5
## - strings    'name' "oh"

## - lists

## Homework:
## Start with this list of numbers:

numbers = [34, 3 ,5, 1, 49]

print(numbers)

## 0. See the length of the list

print( len(numbers) )

## 1/2. print the 4th element of the list


print (numbers[3])

## 1. Change the second number to 11
numbers[1] = 11
print(numbers)

## 2. Check if number 5 is in the list


## 3. Check if number 3 is in the list

## 4. Check as many list functions as you can, and see what they do
numbers.append(45)
print(numbers)

numbers.reverse()
print(numbers)

numbers.append(13)
print(numbers)

numbers.append(55)
print(numbers)

numbers.append(66)
print(numbers)

numbers.append(77)
print(numbers)

numbers.append(5)

numbers.append(5)

numbers.append(11)
print(numbers)

print(numbers.count(11))

print(numbers.count(75))

print(numbers.sort())
print(numbers)

numbers.index()
print(numbers)
