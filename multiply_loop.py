#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in April 2022
# This is the math program, multiplying number from 1 to n


def main():
    # This function multiplies number from 1 to number the user enters

    # input
    multiply_string = input("Enter a positive integer: ")

    # process & output
    loop_counter = 0
    product = 1
    print("")
    try:
        multiply_integer = int(multiply_string)
        if multiply_integer > 0:
            while loop_counter < multiply_integer:
                loop_counter = loop_counter + 1
                product = product * loop_counter
            print("{0}! = {1}".format(multiply_string, product))
        elif multiply_integer == 0:
            print("0! = 1")
        else:
            print("You did not enter a positive number.")
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
