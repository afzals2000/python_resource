from data_structures.user import User


def shallowCopy():
    l1 = [[1,2],3,[4,5]]
    l2 = l1[:]
    print(l1)
    print(l2)

    if (l1 is l2):
        print("l1 and l2 same object {0} <=> {1}".format(id(l1),id(l2)))
    else:
        print("l1 and l2 not same object {0} <=> {1}".format(id(l1),id(l2)))

    if (l1[0] is l2[0]):
        print("l1[0] and l2[0] same object{0} <=> {1}".format(id(l1[0]),id(l2[0])))
    else:
        print("l1[0] and l2[0] not same object {0} <=> {1}".format(id(l1[0]),id(l2[0])))

    l1[0] = [8,9]

    print("after append")
    print("after append")
    print("after append")
    print(l1)
    print(l2)

    if (l1 is l2):
        print("l1 and l2 same object {0} <=> {1}".format(id(l1),id(l2)))
    else:
        print("l1 and l2 not same object {0} <=> {1}".format(id(l1),id(l2)))

    if (l1[0] is l2[0]):
        print("l1[0] and l2[0] same object{0} <=> {1}".format(id(l1[0]),id(l2[0])))
    else:
        print("l1[0] and l2[0] not same object {0} <=> {1}".format(id(l1[0]),id(l2[0])))

def list_sorting():
    # List of Numbers
    list_of_number = [1,2]
    list_of_number.extend([3,4]); list_of_number += ([3,4])  # Modified same list
    new_list_of_number = list_of_number + [6.7]  # Returns a new list

    # List of String
    list_of_fruits = ["banana", "apple", "peach", "mango"]
    print(sorted(list_of_fruits))                           # sorts by natural order and returns a new list
    list_of_fruits.sort(); print(list_of_fruits)            # sorts by natural order in place
    list_of_fruits.sort(key=len); print(list_of_fruits)     # sorts by condition
    list_of_fruits.sort(reverse=True); print(list_of_fruits)     # sorts by condition

    # List of Objects
    Bob = User("Bob", 20); Alice = User("Alice", 30); Leo = User("Leo", 15)
    lu = [Bob, Alice, Leo]
    lu.sort(key=lambda x: x.name); print(*lu, sep="/")  # sort by attribute


def stack_example():
    stack = [1,2,3]
    stack.append(4)  # added to the top
    print(stack.pop())  # pops 4
    print(stack.pop())  # pops 3


if __name__ == "__main__":
    list_sorting()
    stack_example()
    # shallowCopy()
