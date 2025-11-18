class Food():
    def __init__(self, name, rating, type, cuisine):
        self.name = name
        self._rating = rating
        self.type = type
        self.cuisine = cuisine
    
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        if 0 <= value <= 10:
            self._rating = value
        else:
            raise ValueError("Rating must be between 0 and 10")
    
    def __str__(self):
        return f"{self.name} ({self.cuisine} {self.type}) - Rating: {self.rating}/10"
    

class Ranker():
    def __init__(self):
        self.foods = []
    
    def add_food(self, food):
        self.foods.append(food)

    def remove_food(self, food_name):
        self.foods.remove(food_name)
    
    def sort_by_rating(self):
        return sorted(self.foods, key=lambda x: x.rating, reverse=True)
    
    def filter_by_cuisine(self, cuisine):
        return [food for food in self.foods if food.cuisine.lower() == cuisine.lower()]
    
    def filter_by_type(self, type):
        return [food for food in self.foods if food.type.lower() == type.lower()]
    
    def get_top_n(self, n):
        sorted_foods = self.sort_by_rating()
        return sorted_foods[:n]
    
    def get_worst_food(self):
        sorted_foods = self.sort_by_rating()
        return sorted_foods[-1] if sorted_foods else None
    
    def __str__(self):
        return "\n".join(str(food) for food in self.foods)
    

def main():
    ranker = Ranker()
    
    pizza = Food("Pizza", 8.5, "Main Course", "Italian")
    sushi = Food("Sushi", 9.0, "Main Course", "Japanese")
    burger = Food("Burger", 7.5, "Main Course", "American")
    ice_cream = Food("Ice Cream", 8.0, "Dessert", "Various")
    
    ranker.add_food(pizza)
    ranker.add_food(sushi)
    ranker.add_food(burger)
    ranker.add_food(ice_cream)
    
    print("All Foods:")
    print(ranker)
    
    print("\nTop 2 Foods:")
    for food in ranker.get_top_n(2):
        print(food)
    
    print("\nWorst Food:")
    print(ranker.get_worst_food())
    
    print("\nJapanese Foods:")
    for food in ranker.filter_by_cuisine("Japanese"):
        print(food)