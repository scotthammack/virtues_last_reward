KEY = '198449351'
CIPHERTEXT = 'CQUJHNMTEONERAXDFMIOVP' + 'BYOLWXYPXSVZEQGTKRTLED'

index = -1
password = ''

for char in KEY:
	index += int(char)
	if index >= len(CIPHERTEXT):
		index -= (len(CIPHERTEXT) - 1)
	password += CIPHERTEXT[index]

print password
