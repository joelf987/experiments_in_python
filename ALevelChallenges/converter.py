
hexNum = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
def convertToHex (number):
    hex1 = ""
    while (number // 16) > 16:
        hex1 = hexNum[(number % 16)] + hex1
        number = number // 16

    if number < 16:
        hex1 = hexNum[number]
    else:
        hex1 = hexNum[(number // 16)] + hexNum[(number % 16)] + hex1
    print(hex1)
    return hex1


def main():
    number = int(input("Enter a denary / base 10 number: "))
    convertToHex(number)

if __name__ == "__main__":
    main()