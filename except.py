def convert(s):
    try:
        x = int(s)
        print("Conversion succeeded! x = ", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    except TypeError:
        print("Conversion failed!")
        x = -1
    return x

print(convert("6ddd"))

def convert(s):
    try:
        x = int(s)
        print("Conversion succeeded! x = ", x)
    except (ValueError, TypeError):
        print("Conversion failed!")
        x = -1
    return x
