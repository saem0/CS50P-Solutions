def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s[0:2].isdigit():
        return False

    if not 2 <= len(s) <= 6:
        return False

    if s[2] == '0':
        return False

    if s[-1].isdigit() and s[-2].isalpha():
        return False

    if s[-1].isalpha() and s[-2].isdigit() and s[-3].isdigit():
        return False

    if any(char in [",", " ", "-", "_", "?", "/", "."] for char in s):
        return False

    return True


main()
