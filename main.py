def main():
    decision_of_the_next_calculation = False
    while not decision_of_the_next_calculation:
        number_first = int(input("Enter the number A: "))
        number_second = int(input("Enter the number B: "))
        operation = input("Enter a math sign")

        if operation == "+":
            print(number_first + number_second)
        elif operation == "-":
            print(number_first - number_second)
        elif operation == "*":
            print(number_first * number_second)
        elif operation == "/":
            print(number_first / number_second)
        elif operation == "//":
            print(number_first // number_second)
        elif operation == "%" and number_second == 0:
            print(number_first % number_second)
        you_wants_next_calculate = input("If you wants next calculate write t")
        if you_wants_next_calculate == "n":
            end = True
        elif you_wants_next_calculate == "t":
            end = False


if __name__ == "__main__":
    main()
