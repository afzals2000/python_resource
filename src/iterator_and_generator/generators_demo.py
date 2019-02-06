
def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        else:
            counter += 1
            yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def runPipeLine():
    # get first 3 unique numbers
    items = [3, 6, 6, 2, 1, 1]
    for items in take(3, distinct(items)):
        print(items)


def generator_demo():
    # Generator functions allow you to declare a function that behaves like an iterator,
    #   i.e. it can be used in a for loop.
    # If function contains 1 or more yield statement it is Genertor.
    #  return terminates the function entirely
    #  yield statement pauses the function saving all its states and transfers control to the caller
    # Generators takes away the overhead of creating iter and next automatically


    print("Lets take 3")
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):             # => generator, take contains yield
        print(item)

    print("Lets take distinct")
    items = [2, 4, 4, 6, 8, 10]
    for item in distinct(items):
        print(item)

    print("Lets take first 3 distinct")
    items = [3,6,6,2,1,1]
    for item in take(3,distinct(items)):
        print(item)

    print(type([i for i in items]))         # [] => returns List
    print(type((i for i in items)))         # () => generator expression


if __name__ == "__main__":
    generator_demo()
