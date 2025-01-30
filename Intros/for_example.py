#sum the first 10 numbers
sum = 0
for num in range(1,11): #11 is excluded, so it goes from 1 to 10
    sum = sum + num
print(sum)

# print multiplication table
for i in range(1,11):
    for i in range(1,11): # each "for" will finish before going back to iterating making i go from 1 to 2
        print(f"{i} x {j} = {i*j}") #"{}" substitute the value of
    print() # to seperate it with a new line between blocks

# rewrite it using while loop

sum = 0
num = 0
while num < 100:
    num = num + 1
    sum = sum + num #sum += num

