import random

def conv(num):
	orig_num = num

	conv_dict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

	thou = num // 1000
	roman_num = thou * 'M'
	num = num % 1000

	hund = num // 100
	if hund == 9:
		roman_num = roman_num + 'CM'
		hund = 0
	elif hund >= 5:
		roman_num = roman_num + 'D'
		hund = hund - 5
	elif hund == 4:
		roman_num = roman_num + 'CD'
		hund = 0
	roman_num = roman_num + hund * 'C'
	num = num % 100
	
	tens = num // 10
	if tens == 9:
		roman_num = roman_num + 'XC'
		tens = 0
	elif tens >= 5:
		roman_num = roman_num + 'L'
		tens = tens - 5
	elif tens == 4:
		roman_num = roman_num + 'XL'
		tens = 0
	roman_num = roman_num + tens * 'X'
	num = num % 10

	ones = num
	if ones == 9:
		roman_num = roman_num + 'IX'
		ones = 0
	elif ones >= 5:
		roman_num = roman_num + 'V'
		ones = ones - 5
	elif ones == 4:
		roman_num = roman_num + 'IV'
		ones = 0
	roman_num = roman_num + ones * 'I'

	print(orig_num, roman_num)

num = random.randint(100, 5000)
conv(num)

