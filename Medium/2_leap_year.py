n=int(input('Enter Year:'))
if(n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print(f"{n} is leap year.")
else :
    print(f"{n} is not leap year.")