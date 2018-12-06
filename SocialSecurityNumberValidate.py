

def isValid(number):
    return number[1:3].isdigit() and number[5:6].isdigit() and number[8:10].isdigit()


def main():
    
    number = input("Enter a social security number (i.e. ddd-dd-ddd): ").strip()
    if isValid(number):
        print("Valid SSN")
    else:
        print("Invalid SSN")
main()

