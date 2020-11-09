#!/usr/bin/python3

import sys,os

def Traverse(dir):
	for a,b,c in os.walk(dir):
		print(a)
		print(b)
		print(c)
		print('=' * 50)

def main():
	Traverse(sys.argv[1])
if __name__ == '__main__':
	main()

