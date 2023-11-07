# Task 1

# Write and test a function that takes a string as a parameter and returns a sorted list
# of all the unique letters used in the string. So, if the string is cheese, the list
# returned should be ['c', 'e', 'h', 's'].


def main():
    def choice():
        decision = input("\nWould you like to run again? ")
        ans1 = ["Yes", "yes", "YES", "y", "Y"]
        if decision in ans1:
            main()
        else:
            exit()

    def words():
        string = input("Please type in a word: ")
        letters = {x for x in string}

        print(letters)

    words()
    choice()


main()
