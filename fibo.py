"""
Fibonacci number generator
"""
import time
class Fibo:

    def generate_recursive(self, previous, current, count, max):
        if count < max:
            print(current)
            if current == 1 and count == 0:
                return self.generate_recursive(current, current, count+1, max)
            return self.generate_recursive(current, current + previous, count+1, max)

    def generate_with_list(self, max):
        first = 1;
        second = 1;
        results = [];
        if max >= 1:
            results.append(first);
        if max >=2:
            results.append(second);
        for x in range (2, max):
            results.append(first + second);
            first,second = second,results[-1];

        return results;

    """
    Fibonacci series are generated from the sum of the previous two numbers, and start from 1.
    1,1,2,3,5,8...
    """
    def generate(self, max):
        first = 1;
        second = 1;
        for x in range (0, max):
            if x <= 1:
                yield 1;
            else:
                current = first + second;
                yield current;
                first,second = second,current;



def main():
    a = int(input("How many fibonacci numbers? "))
    start = time.time()
    result = Fibo().generate_with_list(a);
    end = time.time()
    print("Time to build a list: %.7f" % (end - start))
    print( "First ", a, " Fibonacci numbers:")
    print("Collected in a list:")
    for x in result:
        print(x)
    start = time.time()
    print("Recursive:")
    Fibo().generate_recursive(1, 1, 0, a)
    end = time.time()
    print("Time to build by recursion: %.7f" % (end - start))
    start = time.time()
    print("Python Generator:")
    for x in Fibo().generate(a):
        print(x)
    end = time.time()
    print("Time to generate: %.7f" % (end - start))


if __name__ == "__main__":
    main()
