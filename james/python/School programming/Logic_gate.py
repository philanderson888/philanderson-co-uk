logic_gate = input("Enter a Logic Gate: AND, OR, XOR, NAND, NOR: ")
num1 = input("Enter either 1 or 0: ")
num2 = input("Enter either 1 or 0: ")


if num1 == "1" or num1 == "0":
    if num2 == "1" or num2 == "0":
        if logic_gate == "OR":
            if num1 == "1" and num2 == "0":
                print("1")
            elif num1 and num2 == "0":
                print("0")
            elif num1 or num2 == "1":
                print("1")

        if logic_gate == "AND":
            if num1 == "1" and num2 == "1":
                print("1")
            else:
                print("0")

        if logic_gate == "XOR":
            if num1 == "1" and num2 == "0":
                print("1")
            else:
                print("0")

        if logic_gate == "NAND":
            if num1 == "1" and num2 == "1":
                print("0")
            else:
                print("1")

        if logic_gate == "NOR":
            if num1 == "1" and num2 == "0":
                print("0")
            elif num1 and num2 == "0":
                print("1")
            elif num1 or num2 == "1":
                print("0")
    else:
        print("Please try again")
else:
    print("Please try again")
