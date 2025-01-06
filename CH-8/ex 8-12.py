def make_sandwiches(*fillings):
    print("The fillings for the sandwich are: ")
    for filling in fillings:
        print(f"\n-\t{filling}")

    print("\nThank you for ordering a sandwich at Om's Shop.\n")

make_sandwiches("Cheese", "Peas", "Tomatoes", "Carrot")
make_sandwiches("Bread", "Cheese", "Cucumber")
make_sandwiches("Bread")
