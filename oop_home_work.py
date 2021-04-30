class Furniture:
    def __init__(self, height, widht, length, color):
        self.height = height
        self.widht = widht
        self.length = length
        self.color = color
        self.area = widht * length
        self.volume = height * widht * length

class Cupboard(Furniture):
    def __init__(self, height, widht, length, color, type_tree):
        super().__init__(height, widht, length, color)
        self.type_tree = type_tree

class Sofa(Furniture):
    def __init__(self, height, widht, length, color, material):
        super().__init__(height, widht, length, color)
        self.material = material

class Table(Furniture):
    def __init__(self, height, widht, length, color, appointmrnt):
        super().__init__(height, widht, length, color)
        self.appointmrnt = appointmrnt

cup_1 = Cupboard(2, 1, 3, 'braun', 'oak')
sofa_1 = Sofa(1, 2, 2, 'red', 'leather')
table_1 = Table(1, 1.5, 2, 'green', 'kitchen')