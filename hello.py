#!/usr/bin/env python
print("hello")

def hello():
    print("hello")


def ab(x):
    if x >= 0:
	return x 
    else:
	return -x
    
if __name__== '__main__':
    hello()
    print(ab(-3))
