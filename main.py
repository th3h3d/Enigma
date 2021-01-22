from collections import deque

class Enigma(object):

	def __init__(self):
		self.R1F = deque(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
		self.R1E = deque(['G', 'H', 'E', 'F', 'V', 'W', 'X', 'Y', 'Z', 'I', 'J', 'Q', 'R', 'S', 'T', 'U', 'A', 'B', 'C', 'D', 'K', 'L', 'M', 'N', 'O', 'P'])
		self.R2F = deque(['L', 'F', 'A', 'C', 'D', 'I', 'G', 'S', 'B', 'P', 'N', 'Q', 'E', 'H', 'X', 'O', 'Z', 'T', 'K', 'V', 'R', 'Y', 'W', 'M', 'U', 'J'])
		self.R2E = deque(['M', 'H', 'L', 'I', 'V', 'Y', 'S', 'Z', 'K', 'E', 'U', 'J', 'X', 'Q', 'C', 'F', 'W', 'O', 'D', 'N', 'P', 'A', 'R', 'T', 'B', 'G'])
		self.R3F = deque(['X', 'F', 'A', 'M', 'T', 'W', 'D', 'V', 'H', 'B', 'I', 'N', 'U', 'K', 'R', 'L', 'G', 'Y', 'S', 'Z', 'P', 'E', 'C', 'J', 'Q', 'O'])
		self.R3E = deque(['E', 'C', 'V', 'O', 'M', 'R', 'K', 'F', 'L', 'N', 'W', 'B', 'I', 'X', 'P', 'J', 'G', 'Q', 'T', 'S', 'D', 'A', 'Z', 'Y', 'H', 'U'])
		self.rotor1PointerKeeper = 0
		self.rotor2PointerKeeper = 0
		self.rotor3PointerKeeper = 0

	
	def setRotorPositions(self,R1,R2,R3):
		self.rotor1PointerSet(R1)
		self.rotor2PointerSet(R2)
		self.rotor3PointerSet(R3)

	def rotor1PointerSet(self, value):
		print("[Info] Rotor 1 is set!")
		if value > 26 or value < 1:
			print("[Error] Rotor 1 Pointer should be between 1-26")
		else:
			self.R1E.rotate(value)
			self.R2F.rotate(value)


	def rotor2PointerSet(self,value):
		print("[Info] Rotor 2 is set!")
		if value > 26 or value < 1:
			print("[Error] Rotor 2 Pointer should be between 1-26")
		else:
			self.R2E.rotate(value)
			self.R2F.rotate(value)

	def rotor3PointerSet(value):
		print("[Info] Rotor 3 is set!")
		if value > 26 or value < 1:
			print("[Error] Rotor 3 Pointer should be between 1-26")
		else:
			self.R3E.rotate(value)
		
		

	def rotor1PointerSet(self, value):
		print("[Info] Rotor 1 is set!")
		if value > 26 or value < 1:
			print("[Error] Rotor 1 Pointer should be between 1-26")
		else:
			self.R1E.rotate(value)
			self.R2F.rotate(value)


	def rotor2PointerSet(self,value):
		print("[Info] Rotor 2 is set!")
		if value > 26 or value < 1:
			print("[Error] Rotor 2 Pointer should be between 1-26")
		else:
			self.R2E.rotate(value)
			self.R2F.rotate(value)

	def rotor3PointerSet(self,value):
		print("[Info] Rotor 3 is set!")
		if value > 26 or value < 1:
			print("[Error] Rotor 3 Pointer should be between 1-26")
		else:
			self.R3E.rotate(value)
			
	def walkThrough(self,userInput):
		print("[Info] Rotors are working!")
		
		self.R1E.rotate(1)
		self.R2F.rotate(1)
		
		self.rotor1PointerKeeper = self.rotor1PointerKeeper + 1
		
		if self.rotor1PointerKeeper == 3:
			self.R2E.rotate(1)
			self.R3F.rotate(1)
			self.rotor1PointerKeeper = 0
			self.rotor2PointerKeeper = self.rotor2PointerKeeper + 1
		else:
			pass
			
		if self.rotor2PointerKeeper == 3:
			self.R3E.rotate(1)
		else:
			pass
			

		print("-INPUT: "+userInput)
		
		
		LETTER_on_R1F = userInput
		
		#R1
		index_of_R1F = self.R1F.index(LETTER_on_R1F)
		
		LETTER_on_R1E = self.R1E.__getitem__(index_of_R1F)

		#R2
		index_of_R2F = self.R2F.index(LETTER_on_R1E)
		
		LETTER_on_R2E = self.R2E.__getitem__(index_of_R2F)
		
		#R3
		index_of_R3F = self.R3F.index(LETTER_on_R2E)
		
		LETTER_on_R3E = self.R3E.__getitem__(index_of_R3F)
		
		
		print("-OUTPUT: "+LETTER_on_R3E)
	
	
	def run(self):
		position_R1 = input("Please Enter 1.Rotor Position:")
		position_R2 = input("Please Enter 2.Rotor Position:")
		position_R3 = input("Please Enter 3.Rotor Position:")
		self.setRotorPositions(int(position_R1),int(position_R2),int(position_R3))
		while(True):
			userInput = input("Enter Your Letter:")	
			self.walkThrough(userInput.upper())


test_instance = Enigma()
test_instance.run()
