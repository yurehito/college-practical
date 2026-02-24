# Question 40:
# Write a class-based program implementing static members.

class Counter:
    count = 0  # Static/class variable
    
    def __init__(self):
        self.id = Counter.count
        Counter.count += 1
    
    def get_id(self):
        return self.id
    
    @staticmethod
    def get_count():
        return Counter.count

# Main program
a = Counter()
b = Counter()
c = Counter()

print(f"IDs: {a.get_id()}, {b.get_id()}, {c.get_id()}")
print(f"Total objects: {Counter.get_count()}")
