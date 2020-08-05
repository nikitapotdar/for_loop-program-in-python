'''Program to check palindrome

Write a program to test if a string of maximum
allowable length of 30 characters is palindrome.
Input -> word
output -> 'Given word is (/not)a palindrome'
'''
#program code starts below
print('Program to check if word is palindrome')
word = input('input the word here (max length 30) : ').upper() or ' '
#upper() is used to convert the whole string into uniformly upper case
x = '' #x initialized to none i.e. empty string
if word != ' ' or len(word) > 30:
      for i in word:
            x = i + x
            #print(x) #remove '#' before print to understand how it works
      else:
            if x == word:
                  print(f'{word} is palindrome')
            else:
                  print(f'{word} is not palindrome')
else:
      print("word can't be blank or longer than 30")
