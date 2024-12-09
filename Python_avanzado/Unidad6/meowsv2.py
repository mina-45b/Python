#Mejora del ejemplo meows

class Cat:
    MEOWS = 3
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
            
            
cat = Cat()

cat.meow()