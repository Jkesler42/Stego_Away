with open("test.png", "rb") as f:
	byte = f.read(1)
	while byte:
		print(byte)
		byte = f.read(1)