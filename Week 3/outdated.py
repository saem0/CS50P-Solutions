months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def get_month(month):

    if month.isdigit():
        return int(month)
    else:
        return months.index(month) + 1

def main():
    while True:
        date = input("Date: ")

        parts = date.split()

        if '/' in date:
            try:
                month, day, year = map(int, parts[0].split('/'))
            except ValueError:
                continue

        elif ',' in date:
            try:
                day = int(parts[1].rstrip(','))
                month = get_month(parts[0])
                year = int(parts[2])
            except ValueError:
                continue
        else:
            continue

        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        else:
            continue

if __name__ == "__main__":
    main()
