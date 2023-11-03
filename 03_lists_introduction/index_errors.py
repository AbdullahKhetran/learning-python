# IndexError: list index out of range

# we start counting from 1, but in python list index starts from 0. So the first item in list is at index 0

motorcycles = ['honda', 'yamaha', 'suzuki']
# this will result in error, because there is no 4th item in list
# print(motorcycles[3])

# if you want to access last item, just use negative index
print(motorcycles[-1])

# negative index can cause error when list is empty
cars: list[str] = []
# error here
# print(cars[-1])
