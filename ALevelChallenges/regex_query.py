import re
def checkString(inputString, inputRegex):
    pattern = re.compile(inputRegex)
    assert len(inputString) > 0, "Input string cannot be empty!"
    return pattern.findall(inputString)

def main():
    inputString = str(input("Enter the sentence you want to check with Regex:  "))
    inputRegex = input("Enter the Regex check: ")
    try:
        result = checkString(inputString, inputRegex)
        if result:
            print("Matches found:\n", result)
        else:
            print("No matches found in ", inputString, " matching ", inputRegex)
    except Exception as e:
        print("Invalid regex: ", e)


if __name__ == "__main__":
    main()


