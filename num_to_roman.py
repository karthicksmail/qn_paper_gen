import random

def convert(num, div):
	conv_dict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
	
	rn = ""
	hund = num // div # When div is 100, 
	if hund == 9:
		rn = rn + (conv_dict[div] + conv_dict[div * 10]) # this is 'CM',
		hund = 0
	elif hund >= 5:
		rn = rn + (conv_dict[div * 5]) # this is 'D',
		hund = hund - 5
	elif hund == 4:
		rn = rn + (conv_dict[div] + conv_dict[div * 5]) # this is 'CD',
		hund = 0
	rn = rn + hund * (conv_dict[div])# and this is 'C'
	num = num % div
	return (rn, num)

def conv(num):
	orig_num = num

	thou = num // 1000
	roman_num = thou * 'M'
	num = num % 1000

	# Start from highest to lowest
	for div in [100, 10, 1]:
		(rn, num) = convert(num, div)
		roman_num = roman_num + rn

	#print(orig_num, roman_num)
	print(roman_num)

num = random.randint(100, 5000)
conv(num)

