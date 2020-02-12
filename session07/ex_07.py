import math

def mysqrt(a):
    while True:
        x = a /2
        y = (x + a / x) / 2
        print(y)
        if x == y:
            break
        x = y

mysqrt(5)

# def main():
    # mysqrt(5)

# if __name__ == "__main__":
#     main()
