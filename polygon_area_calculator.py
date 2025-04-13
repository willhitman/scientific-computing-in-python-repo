class Rectangle:
    width: int
    height: int
    
    def __init__(self, *args):
        if len(args) < 2:
            raise ValueError(f'Shape must take two dimesion but {len(args)} was given')
        
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")

        if any (arg <= 0 for arg in args):
            raise TypeError("Either dimension can be equal or less than 'zero' ")

        self.width = args[0]
        self.height = args[1]
    
    def __str__(self):
        result = f'{self.__class__.__name__}(width={self.width}, height={self.height})'
        return result

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
    
        output_string = "\n".join(["*" * self.width for _ in range(self.height)])
        return output_string + "\n"

    def get_amount_inside(self, shape):
        times = float(self.get_area()) // float(shape.get_area())
        return times
    


class Square(Rectangle):
    #initialize the class
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.height = height
        self.width = height

    def __str__(self):
        result = f'Square(side={self.width})'
        return result

rect = Rectangle(6, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

sq.set_width(20)
print(sq)

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
