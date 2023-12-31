from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for current_product in self.products:
            if current_product.name == product_name:
                return current_product

    def remove(self, product_name: str):
        for current_product in self.products:
            if current_product.name == product_name:
                self.products.remove(current_product)

    def __repr__(self):
        result = []

        for product in self.products:
            result.append(f"{product.name}: {product.quantity}")

        return "\n".join(result)
