import os, random, string, sys

#*******PASSWORDS*******
#password requirements
length = int(sys.argv[2]) #total length of password
num_length = 5 #number of integer characters
symbol_length = 5 #number of punctuation characters
char_length = length - num_length - symbol_length #number of letters

#define character sets
chars = string.ascii_letters
nums = string.digits
symbols = ''
def make_symbols():
	n = string.punctuation
	n = n.replace(',','')
	n = n.replace("'",'')
	n = n.replace("\"",'')
	n = n.replace("!",'')
	return n

#generator
j = 0
while j < int(sys.argv[1]):
	random.seed = (os.urandom(65536))
	chars = string.ascii_letters
	nums = string.digits
	symbols = make_symbols()
	s = ''
	temp_s = ''
	x = 0
	while x < num_length: #choose numbers
		rand_char = random.choice(nums)
		nums = nums.replace(rand_char,"")
		temp_s = temp_s + rand_char
		x += 1
	x = 0
	while x < symbol_length: #choose symbols
		rand_char = random.choice(symbols)
		symbols = symbols.replace(rand_char,"")
		temp_s = temp_s + rand_char
		x += 1
	x = 0
	while x < char_length: #choose letters
		rand_char = random.choice(chars)
		chars = chars.replace(rand_char,"")
		temp_s = temp_s + rand_char
		x += 1
	while len(s) < length: #scramble chosen number, letters, and symbols
		rand_char = random.choice(temp_s)
		temp_s = temp_s.replace(rand_char,"")
		s = s + rand_char
	print s
	j += 1
