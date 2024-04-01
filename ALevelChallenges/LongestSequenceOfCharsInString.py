def longest(chars):
    currentSeqLength = 0
    longestSeq = 0
    longestSeqChar = None
    currentChar = None
    prevChar = None
    for i in range (0, len(chars)):
        currentChar = chars[i]
        if currentChar == prevChar:
            currentSeqLength += 1
            if currentSeqLength > longestSeq:
                longestSeq = currentSeqLength
                longestSeqChar = currentChar
        else:
            currentSeqLength = 1
            if currentSeqLength > longestSeq:
                longestSeq = currentSeqLength
                longestSeqChar = currentChar

        prevChar = currentChar

    return (longestSeq, longestSeqChar)



if __name__ == '__main__':
    inputString = str(input("Enter a string:\n"))
    longestSeq = longest(inputString)
    print("Longest seq of chars in ", inputString, " is ", longestSeq[0], " for char ", longestSeq[1])