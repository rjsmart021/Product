class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")


class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print(f"Specifications: {self.specs}")


class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")


# Test the functionality
if __name__ == "__main__":
    # Create instances of each subclass
    my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
    my_electronic = Electronic("456", "Smartphone", 399.99, "6.7-inch display, 128GB storage")
    my_clothing = Clothing("789", "T-shirt", 19.99, "Large")

    # Display information for each product
    print("Book Information:")
    my_book.display_info()
    print("\nElectronic Information:")
    my_electronic.display_info()
    print("\nClothing Information:")
    my_clothing.display_info()
