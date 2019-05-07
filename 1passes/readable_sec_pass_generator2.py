import os, random, string, sys

#*******PASSWORDS*******
#password requirements
length = 2 #total length of password
num_length = 1 #number of integer characters
symbol_length = 1 #number of punctuation characters
char_length = length - num_length - symbol_length #number of letters

#define character sets
word_file = "/usr/share/dict/words"
#word_file = "/Users/joshualetzter/Desktop/1passes/EOWL-v1.1.2/LF Delimited Format/EOWL_all.txt"
WORDS = open(word_file).read().splitlines()

chars = string.ascii_letters
nums = string.digits
symbols = ''
def make_symbols():
	n = string.punctuation.replace(",","")
	n = n.replace("\"","")
	n = n.replace("=","")
	n = n.replace("\'","")
	n = n.replace("-","")
	n = n.replace("-","")
	n = n.replace("+","")
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
	k = x = 0
	word_num = 3
	while k < word_num:
		rand_word_1 = random.choice(WORDS)
		while (len(rand_word_1) < 3) or (len(rand_word_1) > 6):
			rand_word_1 = random.choice(WORDS)
		s = s + rand_word_1 + " "
		k += 1
	print s
	j += 1
