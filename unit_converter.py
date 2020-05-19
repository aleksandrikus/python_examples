print("Hi, welcome to unit converter! This program converts kilometers to miles.")


def unitconverter():
    k = int(input("Enter number of kilometers: "))
    m = k * 0.621371
    print(str(k) + " km equals " + str(m) + " miles")
    print("Would you like to do another conversion?")
    answer = str(input("Y/N: "))
    return answer


x = unitconverter().lower()

while True:
    if x == "y" or x == "yes":
        x = unitconverter().lower()
    else:
        print("Thank you for using our converter!")
        break

