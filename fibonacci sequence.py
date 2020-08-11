# Program to display the fibonacci seequence of numbers up to n-th term

# Asks user to input the number of terms to be displayed
n = int(input("Number of terms to display: "))

# Initializing first two terms
a = 0
b = 1

print (a)
print (b)

# Loop to print the next terms
for n in range(0, n):
    c = a + b
    print (c)
    # Updation
    a = b
    b = c
