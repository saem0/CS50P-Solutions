while True:
    try:
        fraction = input("Fraction: ")

        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if x > y:
            continue

    except ValueError:
        continue
    except ZeroDivisionError:
        continue

    output = round((x / y) * 100)

    if output <= 1:
        print("E")
    elif output >= 99:
        print("F")
    else:
        print(f"{output}%")
    break
