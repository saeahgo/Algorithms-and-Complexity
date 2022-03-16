import time

def string_matching(text, pattern):
    i = 0 # text index
    j = 0 # pattern index

    for i in range(len(text)):
        if len(text[i:]) < len(pattern):
            break

        length = 0

        for j in range(len(pattern)):
            if(text[i+j] != pattern[j]):
                break
            if text[i + j] == pattern[j]:
                length += 1

        if length == len(pattern): # if pattern matches with texts
            k = 0
            print("P = ", end='')
            while(k < i):
                print("_", end ='')
                k += 1
            print(pattern, end = '')
            while(k < len(text)-len(pattern)):
                print("_", end = '')
                k += 1
            print(" ...[match!]")
            return i
        elif length > 0 and length != len(pattern):
            k = 0
            print("P = ", end='')
            while(k < i):
                print("_", end='')
                k += 1
            if length == 1:
                print(text[k], end = '')
                k += 1
            else:
                l = k
                while(k < l + length):
                    print(text[k], end='')
                    k += 1    
            while(k < len(text)):
                print("_", end = '')
                k += 1
            print(" ")
        else: 
            print("P = ", end='')
            k = 0
            while(k < i):
                print("_", end ='')
                k += 1
            print(text[i], end = '')
            while(k < len(text)-1):
                print("_", end = '')
                k += 1
            print(" ")

text = []
text = input("Enter a text: ")
pattern = []
pattern = input("Enter a pattern find in the texts: ")
print("T =", text)

start = time.time()
match_index = string_matching(text, pattern)
finish = time.time()

print("Match Index:", match_index)
print("Run Time: %fs"%(finish - start))