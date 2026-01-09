text = input("Enter a string:")
rev_text =""
for char in text:
    rev_text= char + rev_text
    
print(f"Reversed string : {rev_text}")