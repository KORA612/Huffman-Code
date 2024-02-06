# Huffman Code

# Note : In this project the main focus is on writing this program in a "step by step" manner.

# Mode 1 : Compression
# 0. Read the input file
# 1. Finding character frequency
# 2. Implementimg priority queue with linked list
# 3. Building the Huffman tree
# 4. Giving each character with their respective binary sequence
# 5. Create output file with first line as reconstruction table and second line as encoded text

# Mode 2 : Decompression
# 1. read, until it makes sense :)


import tkinter as tk
from tkinter import filedialog


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.left = None
        self.right = None


class priorityQueue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, key, value):
        new_node = Node(key, value)
        if self.isEmpty() or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next and curr.next.value <= value:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

    def enqueueNode(self, inpNode):
        if self.isEmpty() or inpNode.value < self.head.value:
            inpNode.next = self.head
            self.head = inpNode
        else:
            curr = self.head
            while curr.next and curr.next.value <= inpNode.value:
                curr = curr.next
            inpNode.next = curr.next
            curr.next = inpNode

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Priority queue is empty")
        temp = self.head
        self.head = self.head.next
        return temp

    def peek(self):
        if self.isEmpty():
            raise Exception("Priority queue is empty")
        return self.head

    def print_queue(self):
        """Prints the elements of the queue in priority order."""
        curr = self.head
        while curr:
            print((curr.key, curr.value), end=" -> ")
            curr = curr.next
        print("None")

    def len(self):
        """Counts the number of elements in the queue."""
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count


def browse_and_select():
    filepath = filedialog.askopenfilename()
    if filepath:
        print(f"Selected file: {filepath}")
        Mode1(filepath)
# 1.1


def frequency(inp):
    frequency = {}
    for character in inp:
        if not character in frequency:
            frequency[character] = 0
        frequency[character] += 1
    return frequency

# 1.2


def makePQ(freq):
    PQ = priorityQueue()
    for key in freq:
        PQ.enqueue(key, freq[key])
    return PQ

# 1.3


def HuffmanTree(PQ):
    root = None
    while (PQ.len() > 1):
        node1 = PQ.dequeue()
        node2 = PQ.dequeue()

        sumNode = Node(node1.key + node2.key, node1.value + node2.value)
        sumNode.left = node1
        sumNode.right = node2

        root = sumNode

        PQ.enqueueNode(sumNode)
    return root

# 1.4


def binarySequencing(node, cstr):
    if node == None:
        return

    if (len(node.key) == 1):
        encoded[node.key] = cstr
        return

    binarySequencing(node.left, cstr + "0")
    binarySequencing(node.right, cstr + "1")


# 1.5
encoded = {}


def Mode1(filepath):
    with open(filepath, "r") as inf:
        inp = inf.read()         # 1.0
    inf.close()

    freq = frequency(inp)         # 1.1

    PQ = makePQ(freq)             # 1.2
    # PQ.print_queue() # See each character in order of how many times they appeared.
    root = HuffmanTree(PQ)        # 1.3
    # PQ.print_queue() # See every character used and total character count.
    binarySequencing(root, "")  # 1.4

    encodedText = ""
    for character in inp:
        encodedText += encoded[character]

    reconstructionTable = ""
    for key in encoded:
        reconstructionTable += key+encoded[key]

    outp = reconstructionTable + "\n" + encodedText

    with open("output.txt", "w") as outf:
        outf.write(outp)
    outf.close()


root = tk.Tk()
root.title("File Browser")

button_font = ("Arial", 32, "bold")
button_width = 20
button_height = 2
browse_button = tk.Button(root, text="Browse", command=browse_and_select,
                          font=button_font, width=button_width, height=button_height)
browse_button.pack()

browse_button.configure(bg="#223843", fg="#dbd3d8",
                        highlightbackground="#ffffff",)

root.mainloop()
