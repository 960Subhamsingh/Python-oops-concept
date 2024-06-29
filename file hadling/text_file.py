# Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory 
# Random Access Memory we use files for future use of the data by permanently storing them.

file = open('text_file1.txt','x') # create a file
 
file.write('Hello programmer')
file.close()

# read the entire text file 

file1 = open('text_file.txt')
file1.read()