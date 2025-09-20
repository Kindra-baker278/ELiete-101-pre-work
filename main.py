print('welcome to the bakery special ordering chatbot')
name= input('What is your name?')
age = int(input('Hello' + name + ',how old are you'))
if age<14:
 print ('too young to order form our bakery, ask a parent or gaurdian')
elif age<18:
 print('Ask adult permission before buying, press next to order')
elif age>75:
 print('Please comfirm witha younger adult if your order is correct')
elif age>18:
 print('Every adut deserves a tasty treat')
else:
 print('you must be an alien')

print('what would you like to order')
def order_menu():
  print("n/---main Menu---")
  print('1.cake slices & cake')
  print('2.pastries')
  print('3.special cake orders')
  print('4.cofee and and appetizers')
  menu_choice = input('>'). lower()