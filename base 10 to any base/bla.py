def transform(n, b):
    if n >= b:
        transform(n//b,b)
    print(n%b)

transform(75,16)