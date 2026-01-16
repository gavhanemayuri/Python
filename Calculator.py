# simple calculator

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int (input("enter your choice (1-4):"))

if choice == 1:
    print("Result:",a+b)
elif choice ==2:
    print("Result:",a-b)
elif choice == 3:
    print("Result:",a*b)
elif choice == 4:
    if b != 0:
        print("Result:",a/b)
    else:
        print("Division by zero not allowed")
else:
        print("Invalid choice")



#********************2️⃣ Leap Year Program (Python)************************

Year = int(input("enter a year:"))

if (Year % 400 == 0) or (Year % 4==0 and Year % 100 !=0):
    print(Year,"is a leap Year")
else:
    print(Year,"is not a leap year")


# ...........................3️⃣ String Count Program........................

text = input("Enter a string: ")

# Character count
char_count = len(text)

# Word count
word_count = len(text.split())

# Vowel count
vowels = "aeiouAEIOU"
vowel_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1

print("Characters:", char_count)
print("Words:", word_count)
print("Vowels:", vowel_count)
