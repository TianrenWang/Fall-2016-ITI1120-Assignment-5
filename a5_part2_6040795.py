# Course: ITI 1120
# Assignment # 5 Part 2
# Wang, Tianren
# 6040795

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:

    def __init__(self, p1, p2, color):
        '''(Rectangle, Point, Point, str) -> None
        Initialize Rectangle with the first point representing the bottom
        left corner of the rectangle and the second representing the top
        right corner of the rectangle, as well as the "color" representing
        the color of the rectangle'''
        
        self.p1 = p1
        self.p2 = p2
        self.color = color

    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation of rectangle
        Rectangle(Point1(x,y), Point2(a,b), "color")'''
        
        return "Rectangle("+str(self.p1)+", "+str(self.p2)+", '"+self.color+"')"

    def get_color(self):
        '''(Rectangle)->str
        Returns the color of the rectangle'''

        return self.color

    def get_bottom_left(self):
        '''(Rectangle)->Point
        Returns the bottom left coordinate of the rectangle'''

        return self.p1

    def get_top_right(self):
        '''(Rectangle)->Point
        Returns the top right coordinate of the rectangle'''

        return self.p2

    def reset_color(self, color):
        '''(Rectangle, str) -> None
        Reset the color of the rectangle to a new color'''
        
        self.color = color

    def move(self, x, y):
        '''(Rectangle, num, num) -> None
        Move the rectangle in the x direction and y direction as the input
        indicates'''

        self.p1.move(x,y)
        self.p2.move(x,y)

    def get_perimeter(self):
        '''(Rectangle) -> num
        Return the perimeter of the rectangle'''

        return abs(self.p1.x - self.p2.x)*2+abs(self.p1.y - self.p2.y)*2

    def get_area(self):
        '''(Rectangle) -> num
        Return the area of the rectangle'''

        return abs(self.p1.x - self.p2.x)*abs(self.p1.y - self.p2.y)

    def contains(self, x, y):
        '''(Rectangle, int, int) -> bool
        Returns whether the point (x,y) is inside of the calling rectangle'''

        return self.p1.x<=x<=self.p2.x and self.p1.y<=y<=self.p2.y

    def intersects(self, other):
        '''(Rectangle, Rectangle) -> bool
        Returns whether the two rectangles in the argument intersect'''

        if self.contains(other.p1.x, other.p1.y) or self.contains(other.p2.x, other.p2.y) or self.contains(other.p1.x, other.p2.y) or self.contains(other.p2.x, other.p1.y):
            return True
        elif (self.p1.x<=other.p1.x<=self.p2.x or self.p1.x<=other.p2.x<=self.p2.x) and (self.p1.y>=other.p1.y and self.p2.y<=other.p2.y):
            return True
        elif (self.p1.y<=other.p1.y<=self.p2.y or self.p1.y<=other.p2.y<=self.p2.y) and (self.p1.x>=other.p1.x and self.p2.x<=other.p2.x):
            return True
        else:
            return False

    def __str__(self):
        '''(Rectangle)->str
        Returns nice string representation in the form of the following:
        I am a "color" rectangle with bottom left corner at p1 and top
        right corner at p2.'''
        return "I am a "+self.color+" rectangle with bottom left corner at ("+str(self.p1.x)+", "+str(self.p1.y)+") and top right corner at ("+str(self.p2.x)+", "+str(self.p2.y)+")."

    def __eq__(self, other):
        '''(Rectangle,Rectangle)->bool
        Returns True if self and other are the same rectangles'''
        return self.p1 == other.p1 and self.p2 == other.p2 and self.color == other.color

class Canvas:

    def __init__(self):
        ''' (Canvas) -> None
        Initialize Canvas with an empty list representing the list of
        rectangles on the canvas.
        '''
        
        self.canvas = []

    def __len__(self):
        ''' (Canvas) -> num
        Returns the size of the canvas.
        '''

        return len(self.canvas)

    def __repr__(self):
        '''(Canvas)->str
        Returns canonical string representation of canvas
        '''
        
        return "Canvas("+str(self.canvas)+")"

    def count_same_color(self, color):
        ''' (Canvas, str) -> int
        Return the number of rectangles on the canvas with the color "color"
        '''

        count = 0

        for rectangle in self.canvas:
            if rectangle.color == color:
                count += 1

        return count

    def add_one_rectangle(self, rectangle):
        ''' (Canvas, Rectangle) -> None
        Add a rectangle to the canvas object.
        '''
        
        self.canvas.append(rectangle)

    def total_perimeter(self):
        ''' (Canvas) -> num
        Returns the sum of the perimeters of the rectangles in the canvas.
        '''

        perimeter = 0
        
        for rectangle in self.canvas:
            perimeter += rectangle.get_perimeter()

        return perimeter

    def min_enclosing_rectangle(self):
        ''' (Canvas) -> Rectangle
        Returns minimum enclosing rectangle that contains all the
        rectangles in the calling canvas.
        '''

        min_x = self.canvas[0].get_bottom_left().x
        min_y = self.canvas[0].get_bottom_left().y
        max_x = self.canvas[0].get_top_right().x
        max_y = self.canvas[0].get_top_right().y
        
        for rectangle in self.canvas:
            if min_x > rectangle.get_bottom_left().x:
                min_x = rectangle.get_bottom_left().x
            if min_y > rectangle.get_bottom_left().y:
                min_y = rectangle.get_bottom_left().y
            if max_x < rectangle.get_top_right().x:
                max_x = rectangle.get_top_right().x
            if max_y < rectangle.get_top_right().y:
                max_y = rectangle.get_top_right().y

        return Rectangle(Point(min_x, min_y), Point(max_x, max_y), "Deep Blue")

    def common_point(self):
        ''' (Canvas) -> bool
        Returns whether there exists a point that intersects all
        rectangles in the calling canvas.
        '''

        for rectangle in self.canvas:
            for another_rec in self.canvas:
                if rectangle is not another_rec and not rectangle.intersects(another_rec):
                    return False

        return True






































    
