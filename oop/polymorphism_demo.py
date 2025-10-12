import math

class Shape:
    """
    Base class representing a geometric shape.
    """
    
    def area(self):
        """
        Calculate the area of the shape.
        
        Raises:
            NotImplementedError: This method must be overridden in derived classes
        """
        raise NotImplementedError("Subclasses must implement area() method")

class Rectangle(Shape):
    """
    Derived class representing a rectangle, inherits from Shape.
    """
    
    def __init__(self, length, width):
        """
        Initialize rectangle attributes.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class representing a circle, inherits from Shape.
    """
    
    def __init__(self, radius):
        """
        Initialize circle attributes.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * self.radius ** 2