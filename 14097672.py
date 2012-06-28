import sys
import os
import Queue
from heapq import *
from collections import defaultdict

# http://www.careercup.com/question?id=14097672

# I have given a Long Sentence and some words(to be searched in the sentence), i have to find the smallest part of the sentence which contains all the words to be Searched in that Sentence and print that part.

# The problem is find the smallest segment of LargeText containing each of the word in SearchWords 
largeText = "a b c d e f d s b c e w e d"
searchWords = ["e", "c", "b"]

# Algorithm:
# The plan is to use store of the indexes of each of the word in search words
# Then construct a min heap from the first elements of each of the word indexes
# Calculate the initial difference between max and min of the heap
# In every iteration, remove the min element of the heap, and insert the next occurence of the word into the min heap.
# Keep track of the segment size when the difference between min and max is less than difference
# When any of the list is empty, break from the loop and output the indexes

if len(searchWords) == 0:
    print "Nothing to search"
    sys.exit(0)

searchWords = set(searchWords)
searchWordsIndexes = defaultdict(lambda: Queue.Queue())
for index, word in enumerate(largeText.split(" ")):
    if word in searchWords:
        searchWordsIndexes[word].put(index)

heap = []
maxIndex = 0
minIndex = sys.maxint
for word,indexQueue in searchWordsIndexes.iteritems():
    try:
        index = indexQueue.get()

        if index > maxIndex:
            maxIndex = index

        if index < minIndex:
            minIndex = index

        heappush(heap, (index, word))
    except IndexError as e:
        print "searchWords don't occur in the input"
        sys.exit(0)

currentDiff = sys.maxint
while(True):

    print heap

    currElement = heappop(heap)
    (minIndex, word) = currElement
    currentDiff = maxIndex - minIndex

    if currentDiff > (maxIndex - minIndex):
        currentDiff = maxIndex - minIndex

    if searchWordsIndexes[word].empty():
        break
    
    try:
        index = searchWordsIndexes[word].get()
    except Queue.Empty:
        print "No more indexes for word"
        break
    
    if index > maxIndex:
        maxIndex = index

    heappush(heap, (index, word))
    heapify(heap)

print minIndex, maxIndex, largeText.split(" ")[minIndex:maxIndex+1]



