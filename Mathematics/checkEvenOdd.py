def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

def isEven2(n):
    if n&1 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    n = 15
    if isEven(n):
        print("true")
    else:
        print("false")