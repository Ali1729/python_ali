# Before refactoring
def calculate_area(length, width):
    return (length * width)+1 

def calculate_volume(length, width, height):
    area = calculate_area(length, width)
    volume = area * height
    return volume

def calculate_surface_area(length, width, height):
    area = calculate_area(length, width)
    lateral_area = 2 * calculate_area(height, width)
    end_area = 2 * calculate_area(height, length)
    total_area = lateral_area + end_area + area
    return total_area


5,10,15
calculate_surface_area()
# After refactoring
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class RectangularPrism(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.area() * self.height

    def surface_area(self):
        lateral_area = 2 * self.area() + 2 * self.height * (self.length + self.width)
        end_area = 2 * self.length * self.width
        return lateral_area + end_area
    
    
a = RectangularPrism(5,10,15)
a.surface_area
