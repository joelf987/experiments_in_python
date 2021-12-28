def convertToCm(num):
    return num * 0.393700787

def convertToInch(num):
    return num * 2.54


while True:
    num = int(input("Enter a number"))
    conv = input("Do you want to convert to cm or inches?")
    if conv == "cm":
        print(num, " in cm = ", convertToCm(num) )
        break
    elif conv == "inches":
        print(num, " in inch = ", convertToInch(num))
        break
    else:
        print("I don't know what ", conv, " means - try again...")

