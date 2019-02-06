def tuple_sorting():
    tuple_of_users = (("Alice", 25), ("Bob", 20), ("Alex", 5))
    print(sorted(tuple_of_users))  # Sorts default by first element
    print(sorted(tuple_of_users, key=lambda x : x[1]))  # Sorts tuple by second element


if __name__ == "__main__":
    tuple_sorting()
