import time


class Factorial:

    def generate_recursive(self, number):
        if number == 0:
            return 1
        else:
            return number * self.generate_recursive(number - 1)

    def generate_loop(self, number):
        result = 1
        for x in range (1, number + 1):
            if (x == 1):
                result = result;
            else:
                result = result * x

        return result;
def main():
    a = -1
    while a < 0:
        a = int(input("Enter a positive number: "))
    # start = time.time()*1000
    # result = Factorial().generate_recursive(a)
    # print("Recursive factorial: ", result)
    # end = time.time()*1000
    # print("Time to build by recursion: %.7f" % (end - start))
    start = time.time()*1000
    result = Factorial().generate_loop(a)
    print("Loop factorial: ", result)
    end = time.time()*1000
    print("Time to build in loop: %.7f" % (end - start))


if __name__ == "__main__":
    main()