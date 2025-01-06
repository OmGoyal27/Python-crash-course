def make_car(manufacture, model, **details):
    details["Manufacture"] = manufacture
    details["Model"] = model
    final_sorted_list = {}

    for key, value in details.items():
        if key == "Manufacture":
            final_sorted_list["Manufacture"] = value
        if key == "Model":
            final_sorted_list["Model"] = value

    for key, value in details.items():
        if key != "Manufacture" or key != "Model":
            final_sorted_list[key] = value

    print("The details of the car are:")
    for key, value in final_sorted_list.items():
        if isinstance(value, str):
            print(f"\n{key.title()} -\t{value.title()}")
        elif isinstance(value, bool):
            print(f"\nIt also has a {key.title()}\n")

make_car("subaru", "outblack", color="blue", tow_package=True)