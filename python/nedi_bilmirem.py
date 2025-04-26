#import string
#
#first_char = input("Enter the first character:")
#second_char = input("Enter the second character:")
#
#def check_characters():
#   if first_char.islower() and second_char.islower():
#      return 1
#   if first_char.isupper() or first_char.islower() and second_char.isupper() or second_char.islower():
#      return 0
#   if first_char and second_char != string.ascii_letters:
#      return -1
#   
#answer = check_characters()
#print(answer)



first_char = input("Enter the first character:")
second_char = input("Enter the second character:")
letters_lower = "abcdefghijklmnopqrstuvwxyz"
letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def check_characters():
   if first_char.islower() and second_char.islower():
      return 1
   if first_char.isupper() or first_char.islower() and second_char.isupper() or second_char.islower():
      return 0
   if first_char and second_char != letters_lower and letters_upper:
      return -1
   
answer = check_characters()
print(answer)