from collections import deque
	
def setRotorPositions(R1,R2,R3):
	rotor1PointerSet(R1)
	rotor2PointerSet(R2)
	rotor3PointerSet(R3)
	


def setAllValues():
	print("[Info] Rotors are ready!")

	
	global R1F
	R1F = deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	
	global R1E
	R1E = deque(['G', 'H', 'E', 'F', 'V', 'W', 'X', 'Y', 'Z', 'I', 'J', 'Q', 'R', 'S', 'T', 'U', 'A', 'B', 'C', 'D', 'K', 'L', 'M', 'N', 'O', 'P'])
	
	
	global R2F
	R2F = deque(['L', 'F', 'A', 'C', 'D', 'I', 'G', 'S', 'B', 'P', 'N', 'Q', 'E', 'H', 'X', 'O', 'Z', 'T', 'K', 'V', 'R', 'Y', 'W', 'M', 'U', 'J'])
	
	global R2E
	R2E = deque(['M', 'H', 'L', 'I', 'V', 'Y', 'S', 'Z', 'K', 'E', 'U', 'J', 'X', 'Q', 'C', 'F', 'W', 'O', 'D', 'N', 'P', 'A', 'R', 'T', 'B', 'G'])
	
	
	global R3F
	R3F = deque(['X', 'F', 'A', 'M', 'T', 'W', 'D', 'V', 'H', 'B', 'I', 'N', 'U', 'K', 'R', 'L', 'G', 'Y', 'S', 'Z', 'P', 'E', 'C', 'J', 'Q', 'O'])
	
	global R3E
	R3E = deque(['E', 'C', 'V', 'O', 'M', 'R', 'K', 'F', 'L', 'N', 'W', 'B', 'I', 'X', 'P', 'J', 'G', 'Q', 'T', 'S', 'D', 'A', 'Z', 'Y', 'H', 'U'])	

	
	global rotor1PointerKeeper
	rotor1PointerKeeper = 0
	
	global rotor2PointerKeeper
	rotor2PointerKeeper = 0
	
	global rotor3PointerKeeper
	rotor3PointerKeeper = 0
	

def rotor1PointerSet(value):
	print("[Info] Rotor 1 is set!")
	if value > 26 or value < 1:
		print("[Error] Rotor 1 Pointer should be between 1-26")
	else:
		global R1E
		R1E.rotate(value)
		global R2F
		R2F.rotate(value)


def rotor2PointerSet(value):
	print("[Info] Rotor 2 is set!")
	if value > 26 or value < 1:
		print("[Error] Rotor 2 Pointer should be between 1-26")
	else:
		global R2E
		R2E.rotate(value)
		global R2F
		R2F.rotate(value)

def rotor3PointerSet(value):
	print("[Info] Rotor 3 is set!")
	if value > 26 or value < 1:
		print("[Error] Rotor 3 Pointer should be between 1-26")
	else:
		global R3E
		R3E.rotate(value)
		
def walkThrough(userInput):
	print("[Info] Rotors are working!")
	global R1F
	global R1E
	global R2F
	global R2E
	global R3F
	global R3E
	
	global rotor1PointerKeeper
	global rotor2PointerKeeper
	global rotor3PointerKeeper
	
	R1E.rotate(1)
	R2F.rotate(1)
	
	rotor1PointerKeeper = rotor1PointerKeeper + 1
	
	if rotor1PointerKeeper == 3:
		R2E.rotate(1)
		R3F.rotate(1)
		rotor1PointerKeeper = 0
		rotor2PointerKeeper = rotor2PointerKeeper + 1
	else:
		pass
		
	if rotor2PointerKeeper == 3:
		pass
		R3E.rotate(1)
	else:
		pass
			
	
	print("-INPUT: "+userInput)
	
	
	LETTER_on_R1F = userInput
	
	#R1
	index_of_R1F = R1F.index(LETTER_on_R1F)
	
	LETTER_on_R1E = R1E.__getitem__(index_of_R1F)

	#R2
	index_of_R2F = R2F.index(LETTER_on_R1E)
	
	LETTER_on_R2E = R2E.__getitem__(index_of_R2F)
	
	#R3
	index_of_R3F = R3F.index(LETTER_on_R2E)
	
	LETTER_on_R3E = R3E.__getitem__(index_of_R3F)
	
	
	print("-OUTPUT: "+LETTER_on_R3E)
	
		
		

	
	
def run():
	setAllValues()
	position_R1 = input("Please Enter 1.Rotor Position:")
	position_R2 = input("Please Enter 2.Rotor Position:")
	position_R3 = input("Please Enter 3.Rotor Position:")
	setRotorPositions(int(position_R1),int(position_R2),int(position_R3))
	while(True):
		userInput = input("Enter Your Letter:")	
		walkThrough(userInput.upper())
		

if __name__ == 'main':
	run()