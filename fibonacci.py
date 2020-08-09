# Program to display the fibonacci seequence of numbers up to n-th term

nterms = int(input("Number of terms to display : "))

# First two terms
n1 = 0
n2 = 1

count = 0
# check if the number of terms is valid
if nterms <= 0:
    print ("Enter a positive integer: ")

elif nterms == 1:
    print ("Fibonacci sequence upto", nterms, ":")
    print (n1)

else:
    print ("Fibonacci sequence: ")
    while count < nterms:
        print (n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1
