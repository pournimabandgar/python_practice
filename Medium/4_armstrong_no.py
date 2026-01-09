#armstrong nymber = 153 = 1*1*1 +5*5*5 + 3 *3*3 = 1 + 125 +27 =153
n=int(input('Enter the number'))
original = n
len_digit =len(str(n))
total = 0 
while n > 0 :
    digit = n % 10
    total += digit**len_digit
    n //=10


if total == original:
    print(f"{original} is Armstrong number")
else:
    print(f"{original} is not Armstrong number")