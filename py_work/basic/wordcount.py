#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().


"""

import sys
import heapq
import operator


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def read_file(file_name):
	file_line = []
	file_content = open(file_name, "rU")
	for line in file_content:
		file_line.extend(line.split())
		#file_line.append(",")
		
		
	file_content.close()	
	return file_line

def print_words(file_name):
	#print read_file(file_name)
	words = []
	lower_words = []
	words = read_file(file_name)
	for words in words:
		lower_words.append(words.lower())
		
	#print sorted(lower_words)
	thin_list = []
	thin_list.append(lower_words[0])
	i = 0
	for word in lower_words:
		if word not in thin_list:
			thin_list.append(word)
			i = i + 1
	
	#print thin_list
	#print len(thin_list) == len(lower_words)
	#thin_list.sort()
	word_count = {}
	for word in sorted(thin_list):
		word_count[word] = 0
		
	for key in word_count.keys():
		i = 0
		for word in lower_words:
			if key == word:
				i = i+1
				#print key
		word_count[key] = i
		
	#for keys in sorted(word_count.keys()):
		#print keys, word_count[keys]	
		
	return word_count	

	
	#print word_count
	
def print_top(file_name):
	#print "not defined yet"
	top_word = {}
	#word_count2 = {}
	word_count = print_words(file_name)
	i = 0		
	for k,v in sorted(word_count.iteritems(), key= operator.itemgetter(1), reverse=True)[:21]:  #Need to understand how operator.itemgetter works'
		i = i+1
		print i,k, v


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
	if len(sys.argv) != 3:
		print 'usage: ./wordcount.py {--count | --topcount} file'
		sys.exit(1)

	option = sys.argv[1]
	filename = sys.argv[2]
	if option == '--count':
		print_words(filename)
	elif option == '--topcount':
		print_top(filename)
	else:
		print 'unknown option: ' + option
		sys.exit(1)

if __name__ == '__main__':
  main()
