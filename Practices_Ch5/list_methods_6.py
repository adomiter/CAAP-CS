#this program converts a sequence of Unicode numbers into a string of text. 

def main():
    print("This program converts a sequence of Unicode numbers into the string of text that it represents. \n")
    
    inString= input("Please enter the Unicode-encoded message: ")
    
    chars= []
    for numStr in inString.split():
        codeNum= int(numStr)
        chars.append(chr(codeNum))
        
    message= "".join(chars)
    print("\nThe decoded message is:", message)
main()