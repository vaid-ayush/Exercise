# Write all content of a given file into a new file by skipping line number 5

with open("test.txt", 'w') as text:
    text.write("line1\n line2 \nline3 \nline4 \nline5 \nline6 \nline7\n")
s=[]
with open("test.txt", 'r') as text:
    s = text.readlines()

    for i in s:
        print(i)
with open("newtext.txt",'w') as t:
    counter=0
    for i in s:
        counter+=1
        if counter == 4:
            continue
        else:
            t.write(i)

