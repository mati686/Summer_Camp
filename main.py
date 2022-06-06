# This is a task project for Oracle Summer Camp.

# Program prints out the numbers 1 to 100 (inclusive).
# If the number is divisible by  3, print "Crackle" instead of the number.
# If it's divisible by 5, print "Pop".
# If it's divisible by both 3 and 5, print "CracklePop".


# Create list on numbers
def create_list (start, stop):
    numbers = list(range(start, stop + 1))
    return numbers

# Substitute numbers divisible by 3, 5 and 15
def substitute (list):
    for i in list:
        if i % 15 == 0:
            list.pop(i-1)
            list.insert(i-1, "CracklePop")
            continue
        if i % 5 == 0:
            list.pop(i-1)
            list.insert(i - 1, "Pop")
        if i % 3 == 0:
            list.pop(i-1)
            list.insert(i - 1, "Crackle")
    return list

if __name__ == '__main__':
    print(substitute(create_list(1, 100)))
