"""
a little program to multiply & divide two numbers
"""
class SimpleCalculator:

    @staticmethod
    def __multiply__(num1, num2):
        """
        I multiply two numbers by repeatedly adding them together.
        :param num1: the first number to multiply.
        :param num2: the second number to multiply.
        :return: the result of multiplication.
        """
        accumulator = 0
        for x in range(0, num2):
            accumulator = num1 + accumulator

        return accumulator

    @staticmethod
    def __divide__(num1, num2):
        """
        I divide two numbers and return the formatted result.
        :param num1: dividend
        :param num2: divisor
        :return: returns the formatted esult
        """
        quotient, remainder = divide(num1, num2)
        return str(quotient) + " r" + str(remainder)

    @staticmethod
    def __modulus__(num1, num2):
        big_num = num1 if (num1 > num2) else num2
        small_num = num2 if (num1 > num2) else num2

        quotient, remainder = divide(num1, num2)

        return remainder

    def __div__(self, num1, num2, decimal_places, rounding=False):
        """
        I divide two numbers up to the number of decimal places specified. I also round
        the result up, if specified.

        :param num1: The dividend
        :param num2: The divisor
        :param decimal_places: Number of decimal places in the result
        :param rounding: Whether the result should be rounded or not
        :return: A string with the formatted result.
        """
        quotient, remainder = divide(num1, num2);

        if remainder == 0:
            return str(quotient) if decimal_places == 0 else str(quotient) + "." + str(remainder)

        decimals = ''
        num1 = self.__multiply__(remainder, 10)

        for x in range(0, decimal_places):
            remainder = self.__modulus__(num1, num2)
            decimals = decimals + str(self.__div__(num1, num2, 0))
            num1 = self.__multiply__(remainder, 10)

        if decimals:
            if rounding:
                last_num: str = decimals[-1]
                num_to_round = decimals[-2]
                decimals = decimals[0:-2]
                if int(last_num) >= 5:
                    num_to_round = str(int(num_to_round) + 1)
            return "{0}.{1}{2}".format(str(quotient), str(decimals), num_to_round)
        else:
            return str(quotient)


def divide(num1, num2):
    """
    I divide two numbers by repeatedly subtracting them until I can't. I then return the result as a tuple of quotient
    and remainder.
    :param num1: dividend
    :param num2: divisor
    :return: returns the result as a tuple of quotient and remainder.
    """
    remainder = num1
    quotient = 0

    while remainder >= num2:
        remainder = remainder - num2
        quotient += 1

    return quotient, remainder


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a, " + ", b, " : ", a + b)
    print(a, " * ", b, ": ", SimpleCalculator.__multiply__(a, b))
    print(a, " / ", b, ": ", SimpleCalculator().__divide__(a, b))
    print(a, " / ", b, ": ", SimpleCalculator().__div__(a, b, 4, True))


if __name__ == "__main__":
    main()
