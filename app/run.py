import sys
mirror_dict = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
		'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
		'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
		'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
		'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

mirror_dict_mini = {k.lower(): v.lower() for k, v in mirror_dict.items()}

def atbash(message):
    cipher = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            if letter in mirror_dict:
                cipher += mirror_dict[letter]
            elif letter in mirror_dict_mini:
                cipher += mirror_dict_mini[letter]
            else:
                cipher += letter
        else:
            # adds space
            cipher += ' '
    return cipher

# Driver function to run the program
def main():
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
        if len(contents) > 0:
            output_file = open('sample.txt', 'a')
            output_file.write(atbash(contents))
            output_file.close()
	

# Executes the main function
if __name__ == '__main__':
	main()
