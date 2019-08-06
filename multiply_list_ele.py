def multiply(numbers):
    total=1
    for i in numbers:
        total=i*total
        print(total)
    return total

print(multiply([2,5,8,7,9]))