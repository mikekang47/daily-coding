import sys

writing = {'a':3, 'b':2, 'c':1, 'd':2, 'e':3, 'f':3, 'g':2, 'h':3, 'i':3, 'j':2, 'k':2, 'l':1, 'm':2, 'n':2, 'o':1, 'p':2, 'q':2, 'r':2,
           's':1, 't':2, 'u':1, 'v':1, 'w':1, 'x':2, 'y':2, 'z':1}

jongmin = sys.stdin.readline().strip()
her = sys.stdin.readline().strip()
new = ''
for i in range(len(jongmin)):
    new += jongmin[i]
    new += her[i]

sequence = []
for i in range(len(new)):
    sequence.append(writing[new[i].lower()])

while len(sequence) > 2:
    temp = []
    for i in range(1,len(sequence)):
        num = sequence[i-1] + sequence[i]
        temp.append(num % 10)
    sequence = temp
print(''.join(list(map(str, sequence))))
