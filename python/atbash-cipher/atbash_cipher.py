from string import ascii_lowercase, digits, maketrans, translate
from re import findall

def encode(string):
	string = ''.join(findall('[a-z0-9]',string.lower()))
	trans_table = maketrans(ascii_lowercase+digits, ''.join(reversed(ascii_lowercase))+digits)
	string = translate(string, trans_table)
	return ' '.join(findall(".{1,5}", string))
def decode(string):
	return encode(string).replace(' ','')