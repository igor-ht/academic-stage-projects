''' Python OOP1 Exercise '''
import copy
from typing import Union

VITAMINS_NUM = 10

#########################################
# Question 1 - do not delete this comment
#########################################
class FoodProduct:
    def __init__(self, name: str, price: float, weight: float, vitamins: str):
        #TODO: write your code here
        self.name = name
        self.price = price
        self.weight = weight
        self.vitamins = vitamins


    def get_total_price(self):
        '''
        Returns the total price of the product: price * weight.
        '''
        #TODO: write your code here
        return self.price * self.weight

    def change_price(self, price: float):
        '''
        Changes the price of the product.
        If the price is non-positive, raises a ValueError.
        '''
        #TODO: write your code here
        if price > 0:
            self.price = price
        else:
            raise ValueError(f'This value is not valid.')

    def __repr__(self):
        '''
        Returns a string representation of the product.
        '''

        return f'Name: {self.name}, Price: {str(self.price)}, Weight: {str(self.weight)}'


    def get_vitamins_num(self) -> int:
        '''
        Returns the number of vitamins in the product.
        '''
        #TODO: write your code here

        return self.vitamins.count('1')

    def combine_product(self, other: 'FoodProduct'):
        '''
        Gets another product of the same type and adds it to the current product.
        That is, adds the weight of the other product to the current product.
        If the products are not the same (name, price, vitamins), raises a ValueError.
        '''
        #TODO: write your code here
        if other.name != self.name or other.vitamins != self.vitamins or other.price != self.price:
            raise ValueError('Can not add products')
        else:
            self.weight = self.weight + other.weight

        
    # to avoid a problem of adding an object to itself, can use this
    def copy(self):
        '''
        Returns a copy of the current product.
        '''
        #TODO: write your code here
        return FoodProduct(self.name, self.price, self.weight, self.vitamins)


#########################################
# Question 2 - do not delete this comment
#########################################
class Furniture:
    def __init__(self, name: str, price: float, amount: int, people: int):
        #TODO: write your code here
        self.name = name
        self.price = price
        self.amount = amount
        self.people = people

    def get_total_price(self):
        '''
        Returns the total price of the product: price * amount.
        '''
        #TODO: write your code here
        return self.price * self.amount
    
    def __repr__(self):
        '''
        Returns a string representation of the furniture.
        '''
        #TODO: write your code here

        return f'Name: {self.name}, Price: {str(self.price)}, Amount: {str(self.amount)}, People: {str(self.people)}'


    def combine_product(self, other):
        '''
        Gets another product of the same type and adds it to the current product.
        That is, adds the amount of the other product to the current product.
        If the products are not the same (name, price, people), raises a ValueError.
        '''
        #TODO: write your code here
        if other.name != self.name and other.people != self.people and other.price != self.price:
            raise ValueError('Can not add products')
        else:
            self.amount = self.amount + other.amount

    # to avoid a problem of adding an object to itself, can use this
    def copy(self):
        '''
        Returns a copy of the current furniture.
        '''
        #TODO: write your code here
        return Furniture(self.name, self.price, self.amount, self.people)

#########################################
# Question 3 - do not delete this comment
#########################################
class ShoppingList:

    def __init__(self, l: list[Union[FoodProduct, Furniture]]):
        self.products = {}
        #TODO: write your code here
        for product in l:
            self.add_product(product.copy())

    def add_product(self, product: Union[FoodProduct, Furniture]):
        '''
        Adds a product to the shopping list.
        If the product is already in the shopping list, combine the two of them.
        '''
        #TODO: write your code here

        if product.name in self.products:
            self.products[product.name].combine_product(product)
        else:
            self.products[product.name] = product.copy()


    def get_products(self) -> list[Union[FoodProduct, Furniture]]:
        '''
        Returns a list of the products in the shopping list.
        '''
        #TODO: write your code here
        return list(self.products.values())





    def remove_product(self, name: str):
        '''
        Removes a product from the shopping list.
        If the product is not in the shopping list, does nothing.
        '''
        #TODO: write your code here
        if name in self.products:
            self.products.pop(name)




    def has_sufficient_v(self, k: int) -> bool:
        '''
        Returns True The shopping list has at least k unique vitamins, False otherwise.
        '''
        #TODO: write your code here
        vitamins = [0] * VITAMINS_NUM
        for product in self.products.values():
            if isinstance(product, FoodProduct):
                for i in range(VITAMINS_NUM):
                    if product.vitamins[i] == '1':
                        vitamins[i] = 1

        return sum(vitamins) >= k

    def get_closest_total_price(self, total_price: float) -> Union[FoodProduct, Furniture]:
        '''
        Returns the product in the shopping list that has the closest total price to the given total price.
        If there are multiple products with the same closest total price, returns one of them.
        If there are no products in the shopping list, returns None.
        Returns a "soft copy" - a pointer to the product object and not a copy of it.
        '''
        #TODO: write your code here
        closest_product = None
        min_distance = float("inf")
        for product in self.get_products():
            cur_dist = abs(product.get_total_price() - total_price)
            if cur_dist < min_distance:
                min_distance = cur_dist
                closest_product = product
        return closest_product

        # if needed to return a copy of the product, you should write:
        # return closest_product.copy()

###################################
# Main - do not delete this comment
###################################
def q1():
    # A
    banana = FoodProduct("Banana", 5.0, 1.0, "0110100101")
    # B
    print(f'The bananas cost {banana.get_total_price():.2f}')
    # C
    banana.change_price(10.0)
    print(f'Due to the draught, the bananas cost now {banana.get_total_price():.2f}')
    # D
    print('This is how a FoodProduct object looks like:')
    print(banana)
    # E
    print(f'The banana has {banana.get_vitamins_num()} vitamins')
    # F
    old_banana = FoodProduct("Banana", 3.0, 4.0, "0110100101")
    apple = FoodProduct("Apple", 3.0, 2.0, "0100101000")
    banana2 = FoodProduct("Banana", 10.0, 2.0, "0110100101")
    banana.combine_product(banana2)
    print(f'After adding more bananas, banana now looks like:\n{banana}')

    #Should raise a ValueError:
    #banana.combine_product(old_banana)
    #banana.combine_product(apple)

def q2():
    # A
    chair = Furniture("Chair", 100.0, 5, 1)
    # B
    print(f'The chairs cost {chair.get_total_price():.2f}')
    # C
    print('This is how a Furniture object looks like:')
    print(chair)
    # D
    sofa = Furniture("Sofa", 1000.0, 1, 3)
    fancy_chair = Furniture("Fancy chair", 300.0, 2, 1)
    chair2 = Furniture("Chair", 100.0, 2, 1)
    chair.combine_product(chair2)
    print(f'After adding more chairs, chair now looks like:\n{chair}')

    # Should raise a ValueError:
    #chair.combine_product(sofa)
    #chair.combine_product(fancy_chair)


def q3():
    # A, B
    l = ShoppingList([
        FoodProduct("Banana", 5.0, 1.0, "0110100101"),
        FoodProduct("Banana", 5.0, 2.0, "0110100101"),
        Furniture("Chair", 100.0, 5, 1),
        Furniture("Sofa", 1000.0, 1, 3)
        ])
    # C
    print(f'The shopping list is:\n{l.get_products()}')
    # D
    l.remove_product("Sofa")
    print(f'After removing the sofa, the shopping list is:\n{l.get_products()}')
    # E
    l.add_product(FoodProduct("Apple", 3.0, 2.0, "0001100000"))
    print('Apples have been added to the shopping list')
    print(f'The shopping list contains at least 6 unique vitamin: {l.has_sufficient_v(6)}')
    print(f'The shopping list contains at least 7 unique vitamin: {l.has_sufficient_v(7)}')
    # F
    print(f'The closest product to the total price of 300 is:\n{l.get_closest_total_price(300)}')
    print(f'The closest product to the total price of 10 is:\n{l.get_closest_total_price(10)}')

if __name__ == '__main__':
    # comment out the questiones you don't want to run
    #q1()
    #q2()
    q3()