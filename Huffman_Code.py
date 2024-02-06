# Huffman Code

# Mode 1 : Compression
# 1. Finding character frequency
# 2. giving each character with their respective binary sequence - using binary tree 
# 3. replacing .txt file with the encoded .cmp file

# Mode 2 : Decompression
# 1. read, until it makes sense :)


inp = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

# 1.1
frequency = {}
for character in inp:
	if not character in frequency:
		frequency[character] = 0
	frequency[character] += 1
print(frequency)