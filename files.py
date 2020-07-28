# Newline character
print('Hello \nWorld')


# Counting lines in a file 
fhand= open('mbox.txt')
count=0
for line in fhand:
    count=count+1
print('Line Count:', count)


# Searching through a file (fixed)
fhand=open('mbox.txt')
for line in fhand:
    line=line.rstrip()
    if line .startswith('From:'):
        print(line)


# Skipping with continue
fhand=open('mbox.txt')
for line in fhand:
    line=line.rstrip()
    if not  line.startswith('From:'):
        continue
    print(line)


# Counting subject lines in mbox.txt/mbox-small.txt
fname=input('Enter the name of  the file: ')
fhand=open(fname)
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There were', count,'subject lines in', fname)


# Counting subject lines in mbox.txt/mbox-small.txt (using try and except)
fname=input('Enter the name of  the file: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There were', count,'subject lines in', fname)


