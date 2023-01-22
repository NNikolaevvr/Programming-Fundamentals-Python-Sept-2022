class Catalogue:
    def __init__(self,name):
        self.name = name
        self.products = []

    def add_product(self, product: str):
        self.products.append(product)

    def get_by_letter(self, first_letter: str):
        return [str(x) for x in self.products if x.startswith(first_letter)]

    def __repr__(self):
        string = f"Items in the {self.name} catalogue:\n"
        string += '\n'.join(sorted(self.products))
        return string


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
