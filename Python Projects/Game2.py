<Player>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

<Ball>:
    canvas:
        Color:
            rgba: 1, 0.55, 0
        Rectangle:
            pos: self.pos
            size: self.size

<Block>:
    Canvas:
        Color:
            rgb: self.colour
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgb: 0.1, 0.1, 0.1
        Line:
            rectangle:
                [self.x, self.y,
                 self.width, self.
    height]
                
