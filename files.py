# READING FILES
# x = open('hello.txt')
# print(x)


# FILE HANDLE AS A SEQUENCE
# - A file handle ipen for read can be treated as a sequence of strings where each line in the file is a string in the sequence.
# xfile = open('hello.txt')
# for i in xfile:
#     print(i)


# COUNTING LINES IN A FILE
fhand = open('hello.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count : ', count)
