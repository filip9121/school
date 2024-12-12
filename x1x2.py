#task 3, given is a set number of integers x1 x2,.. xn write an algorithm that counts how many times the following number is bigger than the previous
def count_increases(numbers):
 if len(numbers)<=1:
    return 0
count=0
def numbers(n):
 for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            count += 1
def new_func(count):
    return count

    return new_func(count)

numbers=[0,1,2,3,4,5,2,7,8]

result=count_increases(numbers)
print("Number of times a number is bigger than the previous:", result)