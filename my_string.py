'''
Given a string like: "A dog ate my cat. The dog was a bad cat eating dog."
Find the number of times "dog" and "cat" occur in the String, and print it out.
'''
sentence = input("please enter a sentence")


substring1 = "dog"
substring2 = "cat"
count1 = string.count(substring1)
count2 = string.count(substring2)

print("The count for dog is", count1)
print("The count for cat is", count2)

def count (string, substring):
    start = 0
    store = str.find(substring, start) + 1
    print(store)




def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a, " + ", b, " : ", a + b)
    print(a, " * ", b, ": ", SimpleCalculator.__multiply__(a, b))
    print(a, " / ", b, ": ", SimpleCalculator().__divide__(a, b))
    print(a, " / ", b, ": ", SimpleCalculator().__div__(a, b, 4, True))


if __name__ == "__main__":
    main()


