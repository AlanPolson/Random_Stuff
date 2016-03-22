def accept_code():
	code = [' ']
	#code.extend(list(raw_input("Enter String you wish to use as \
	#	cipher base: ")))
	code.extend(list("""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn\
	opqrstuvwxyz1234567890,.!?#$%^&*/+-_<>"'"""))
	return code

def encode(code):
	ip = raw_input("Enter words: ")
	ip_list = ip.split()
	ip_letters = []
	for word in ip_list:
		ip_letters.append(list(word))
	encoded=''
	for words in ip_letters:
		for letters in words:
			for index, letter in enumerate(code):
				if letters==letter:
					if index<10:
						indx='0'+str(index)
                	else:
                		indx = str(index)
                	encoded+=indx
    	encoded+='00'
    	return encoded

def decode(code,encoded):
	#dec_in = raw_input("enter string to decode: ")
	dec_in = encoded
	split_str = list(str(dec_in))
	new_indexes = []
	new_indx = 'wrong'
	for index, value in enumerate(split_str):
   		if index%2 == 0:
   			new_indx = value
    	else:
    		new_indexes.append(new_indx+value)
    decoded = []
	for num in new_indexes:
    	number = int(num)
    	for index, value in enumerate(code):
        	if int(number/10)==0:
            	number = number%10
        	if number == index:
        		decoded.extend(value)
    return decoded