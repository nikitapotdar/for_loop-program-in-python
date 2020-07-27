#Program to demostrate Python For... loop
'''Prints all even numbers in the given range

   Write a program to print all the +ve even numbers in
   given range of two numbers. User to input the start
   and end numbers of the range. The end number is to be
   included. Remember that end number by default is excluded
   from the range.
'''
print('Program to print even numbers in positive range')
StartNum = int(input('Input starting number (lower) : ') or 0)
EndNum = int(input('Input ending number (higher) : ') or 0)
if StartNum < EndNum and StartNum >= 0 and EndNum >= 0:
      z = range(StartNum, EndNum + 1)#EndNum + 1 to include the end number
      for i in z:
            if i % 2 == 0:
                  print(i, 'is even number')
      else :
            print(f'all even numbers between {StartNum} and {EndNum}')
else:
      print('Not valid range')
