# Exercise 1

# count = 0

# while (count <=10):
#     print(count, "Olá Mundo!")
#     count +=1


# Exercise 2

# x = 10

# while not(x==0):
#         x-=1
#         if x % 2 !=0:
#             print(x)

# Exercise 3

# i = 1
# n = 10
# while i < n:
#       "iteração"
#       i= i+1



#Exercise 4

terminou = False
p = i = 0

while(not terminou):
    n = int(input("Digite um número, ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 ==0:
            p = p + 1
        else:
            i = i+1
print("P = ", p)
print("I = ", i)
