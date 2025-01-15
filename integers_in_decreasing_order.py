print('Enter three integers')
print()

userinput_one = int(input('Enter first integer: '))
userinput_two = int(input('Enter second integer: '))
userinput_three = int(input('Enter third integer: '))

if (userinput_one < userinput_two < userinput_three):
		print(userinput_one, userinput_two,  userinput_three)
elif userinput_two < userinput_one < userinput_three:
		print(userinput_two, userinput_one, userinput_three)
else:
		print(userinput_three, userinput_one, userinput_two)