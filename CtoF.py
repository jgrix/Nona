#!/usr/bin/python

#Converts centigrade to Freedom units

def C_to_F(cent):
	f = cent * 9
	f = f / 5
	f = f + 32
	return f


if __name__ == "__main__":
	print "Testing function"
	print C_to_F(20)
	print C_to_F(0)
	print C_to_F(100)
