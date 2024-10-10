vow = "aeiouAEIOU" #declaring global variable

ch=input("Enter a character: ")

if ch in vow:
    print(ch,"is a vowel")
else:
    print(ch,"is a consonant")