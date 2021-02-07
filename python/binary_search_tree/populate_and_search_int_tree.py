
# class Node(self, value=None, left=None, right=None):
# 	self.left 

class BinarySearchTree:

	input_file = 'binary_search_tree_data.txt'

	def __init__(self):
		print("BST created!", end='...  ')
		data_file = self.createFile()
		self.populateDataFile(data_file)
		print("BST Populated!")

	def createFile(self, data_file=input_file):
		data = open(data_file, 'w+')
		return data

	def populateDataFile(self, data_file=input_file):
		# num_list = [str(num)+"\n" for num in range(1,11)]
		data_file.writelines(["Hello\n", "world!\n"]) # works!
		# data_file.writelines(num_list)
		return data_file.read()

my_tree = BinarySearchTree()

