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
    
    def get_top_n(self, n):
        sorted_foods = self.sort_by_rating()
        return sorted_foods[:n]
    
    def __str__(self):
        return "\n".join(str(food) for food in self.foods)
    
