grade = int(input())
if 80 <= grade < 90:
    print("B", end="")
elif 60 <= grade < 70:
    print("D", end="")    
if 90 <= grade < 100:
    print("A", end="")
elif 70 <= grade < 80:
    print("C", end="")
if 0 <= grade < 60:
    print("F")
else:
    print("Z")

