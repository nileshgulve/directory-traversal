#!/usr/bin/python3

import sys,os

def Traverse(dir):
	for a,b,c in os.walk(dir):
		print("Current location: ",a)
		print("Folder Inside the current location(",a + "):",b)
		print("Files inside the current location(",a + "):",c)
		print('=' * 70)

def main():
	Traverse(sys.argv[1])
if __name__ == '__main__':
	main()

