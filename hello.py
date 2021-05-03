"""
a little program to say hello
"""
import sys

def main(argv):
	print "Hello {0} and {1}! Lets go to the park {0} and {1}.".format(argv[1], argv[2])

if __name__=="__main__":
	main(sys.argv)
