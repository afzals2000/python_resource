from data_structures.user import User


# It is not possible to sort a dictionary only to get a representation of a sorted element.
# dictionary are inherently orderless, but other types, such as lists and tuples, are not
def copyAndMerge():
    d_numbers = {1: 2, 3: 4, 4 : 3, 2: 1, 0: 0}
    d_sorted_as_list = sorted(d_numbers.items(), key=lambda kv: kv[1])  # returns sorted list of values
    print(type(d_sorted_as_list))


def set_example():
    # sets
    Bob = User("Bob", 20); Alice = User("Alice", 30); Leo = User("Leo", 15)
    set_of_users = {Bob, Alice, Leo}; print(",".join(str(i) for i in set_of_users))
    sorted(set_of_users, reverse=True)  # sorting sets of object.
    print(",".join(str(i) for i in set_of_users))


if __name__ == "__main__":
    # set_example()
    copyAndMerge()

