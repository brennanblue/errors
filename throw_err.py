#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys
import os

def print_usage():
    """Print usage and exit"""
    sys.stderr.write("usage: python raise_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tzerodivision\n")
    sys.exit()

def contains(char_string, char):
# adjust returned index to account for searching in reverse
    return len(char_string) - char_string[::-1].index(char) - 1

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
# raise AssertionError
   # try:
        assert 1==2
   # except AssertionError:
        print 'not likely'
#	exit(1)	
elif error_type == "io":
  #  raise IOError
    file = open('nothere.txt')
    print file
elif error_type == "import":
    import os
    os.chdir ("fail")
    #  from error import testest_foo.py
    #  raise ImportError
elif error_type == "index":
    # dogs = {0: 'racer', 1: 'dixie', 2: 'heela'}
    dogs =[1,2]
    a = dogs[3]
    # raise IndexError
elif error_type == "key":
    array = {a: 'duck', b: 'duck'}
    print array['c']
	#  raise KeyError
elif error_type == "name":
    print what
    #    raise NameError
elif error_type == "os":
    for i in range(9):
        print n

#    raise OSError
elif error_type == "type":
    # raise TypeError
    b = 'dog'
    c = 'cat'
    print (b / c)
elif error_type == "value":
    # raise ValueError
    contains ('atgcaggtacaba', 'k')
elif error_type == "zerodivision":
    print 3.1415926/0
    # raise ZeroDivisionError
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
