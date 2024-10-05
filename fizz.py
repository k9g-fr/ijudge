counter = 1
num = int(input())
while counter <= num:
    if not counter % 15:
        print("FizzBuzz")
        counter = counter+1
    elif not counter % 5:
        print("Buzz")
        counter = counter+1
    elif not counter % 3:
        print("Fizz")
        counter = counter+1
    else:
        print(counter)
        counter = counter+1
