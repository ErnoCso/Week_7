# Task 2

# Write and test three functions that each take two words (strings) as parameters and
# return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words.
# Letters that appear in both words.
# Letters that appear in either word, but not in both.
# Hint: These could all be done programmatically, but consider carefully what topic we
# have been discussing this week! Each function can be exactly one line

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
        res = len(string.split())
        print(str(res))
        print(string.split())

        letters = {x for x in string}
        print(letters)
        print(len(string))

        item1 = {string}
        for item in item1:
            print(item)
            print(len(item))

    words()
    choice()


main()
