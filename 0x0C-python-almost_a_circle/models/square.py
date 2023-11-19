#!/usr/bin/python3
"""Create square class which inherits
from Rectangle class
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class all attributes inherited from
    Rectangle class
    width : size
    height : size
    x
    y
    id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize rectangle attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """override str and make it readable"""
        string = "[Square]"
        string += f" ({self.id}) {self.x}/{self.y}"
        string += f" - {self.width}"
        return string
