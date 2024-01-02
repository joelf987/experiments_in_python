def fizzbuzz(fizzNumber, buzzNumber, number):
    if number<= 0:
        raise Exception("Expected a positive integer - was: ", fizzNumber)

    for i in range(1, number + 1):
        # print("Number: ", i, " is prime: ", isPrime(i))
        if isPrime(i):
            print("Oops!", i)
        elif not (i % (fizzNumber * buzzNumber)):
            print("FizzBuzz: ", i)
        elif i % fizzNumber == 0:
            print("Fizz: ", i)
        elif i % buzzNumber == 0:
            print("Buzz: ", i)


    # print("Checked numbers up to: ", i)
    # if not(divisible):
    #     print("oops!")

def isPrime(number):
    if number == 1:
        return False
    prime = True
    for i in range(2, number):
        prime = number % i != 0
        if not prime:
            return False

    return prime



def main():
    # number = 24
    # print("Is prime ", number, ": ", isPrime(number))
    fizzNumber = int(input("Enter a base number for Fizz: "))
    if fizzNumber not in range(1,10):
        raise Exception("Error- choose a base number between 1 - 9")
    buzzNumber = int(input("Enter a base number for Buzz: "))
    if buzzNumber not in range(1,10):
        raise Exception("Error- choose a base number between 1 - 9")
    number = int(input("Enter any positive integer: "))
    fizzbuzz(fizzNumber, buzzNumber, number)


if __name__ == "__main__":
    main()