from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
from builtins import input

def remove_duplicates(string):
	if string.isalpha():
    	new_string = set(string) 				#sets have no duplicates
    	duplicates_count = len(string) - len(new_string)
    	final_string = sorted( list(new_string))
    	unique_string   = ''.join(final_string)
    	print (unique_string, duplicates_count)
	else :
   	print ('Argument should be a string')

print (‘Give me a string:’,end=' ')
given_str = input()
remove_duplicates(given_str)
