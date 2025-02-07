# A program is whether a leap year or not

year =2000,2001,2002,2003,2004,2005,2006,200,2008,2009,2010
for year in range(2000,2010):
    if year % 4 == 0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")

# A program to check a letter whether it's a consonant or a vowel

letter = "b"
letter_list = letter.split(",")

vowels = "aeiou"
for letter in letter_list :
    if letter in vowels :
        print(letter,"is a vowel")
    else:
        print(letter,"is a consonant")







