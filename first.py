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
        
    
