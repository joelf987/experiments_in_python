def reverse(text):
    reversed = ""
    for i in range(len(text) -1, -1, -1):
        reversed = reversed + text[i]
    return reversed



def main():
    text = str(input("Enter some text: "))
    print("Reversed text: ", reverse(text))


if __name__ == "__main__":
    main()
