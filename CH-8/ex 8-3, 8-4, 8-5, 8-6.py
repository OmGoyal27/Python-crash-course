def make_shirt(size="Large", text="I love Python"):
    print(f"Making a shirt of size {size.title} with text {text.title} printed on it.")

def describe_city(country="India", city=""):
    print(f"{city.title()} is in {country.title()}.")

def city_country(city: str, country: str):
    formatted_string = f"{city.title()}, {country.title()}"
    return formatted_string

class Testing:

    def test_make_shirt():
        make_shirt("Medium", "Om Goyal")
    
    def test_describe_city():
        describe_city("America", "Washington")

    def test_city_country():
        print(city_country("Punjab", "India"))