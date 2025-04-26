eded=int(input("Eded daxil edin:"))
if eded%3==0 and eded%5==0:
    print('FizzBuzz.')
elif eded%3==0:
    print('Fizz.')
elif eded%5==0:
    print('Buzz.')
else:
    print("Eded ne 3-e, ne de 5-e bolunur.")
