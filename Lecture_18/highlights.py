# highlights from lecture 18

def isEven(x):
    result = False
    if x % 2 == 0:
        result = True
    return result

def repeat(phrase, x):
    for v in range(x):
        print(phrase)

def add(a, b):
    return a + b

if __name__ == '__main__':
    repeat("Hello world!", 8)
    repeat("What's up?", 3)
    print(add(7,8))
    print(add("Hello","world"))
    print(add(3.14159, 7.888))


