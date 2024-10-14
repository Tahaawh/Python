# 97 / 122  a,b,c
# 65 / 90  A,B,C 
input_text = "Hi my Name Is tahA and my last NamE iS AhMadi"

lowresult = ""
upresult = ""

for i in input_text:
    if 65 <= ord(i) <= 90:
        u = chr(ord(i)+32)
        lowresult += u
    else:
        lowresult += i

    if 97 <= ord(i) <= 122:
        x = chr(ord(i)-32)
        upresult += x
    else:
        upresult += i
print("\n")
print(f"Lowercase: {lowresult}\nUppercase: {upresult}","\n")

# next code
text = "My Name Is melsam mY aGe Is 40"
tex = ""

for ia in text:
    x = " "
    if 'A' <= ia <= 'Z':
        x = chr(ord(ia) + 32)
        tex += x
    else:
        tex += ia

print(tex,"\n")

# next code 
textq = "Hi my Name Is tahA and my last NamE is AhMadi"

t2 = ""
for ie in textq:
    if 65 <= ord(ie) <= 90:
        u = chr(ord(ie) + 32)
    else:
        u = ie
    t2 += u

t3 = ""
for item in range(len(t2)):
    if item == 0 or t2[item - 1] == " ":
        t3 += chr(ord(t2[item]) - 32)
    else:
        t3 += t2[item]

print(t3)