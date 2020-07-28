# 6.5 Write code using find() and string slicing (see section 6.10) 
# to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text ="X-DSPAM-Confidence: 0.8475"
ipos=text.find(":")
piece=text[ipos+2:]
print(piece)
value=float(piece)


# 7.1 Write a program that prompts for a file name, then opens 
# that file and reads through the file, and print the contents 
# of the file in upper case. Use the file words.txt to produce the 
# output below.

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    lx=line.rstrip()
    print(lx.upper())


# 7.2 Write a program that prompts for a file name, then opens 
# that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of 
# the lines and compute the average of those values and produce an 
# output as shown below. Do not use the sum() function or a variable named 
# our solution.

fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    x=float(line[20:])
    count=count+1
    total=total+x
avg=sum/count
print('Average spam confidence:', avg)

# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# total = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"): 
#         continue
#     t=line.find("0")
#     number= float(line[t:])
#     count = count + 1
#     total = total + number

# average = total/count
# print ("Average spam confidence:",average)