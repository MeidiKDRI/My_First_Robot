class Robot() :

    def __init__(self, name) :
        self.name = name
        self.direction = 'Est'
        self.x = 0
        self.y = 0

    def forward(self) :
        if self.direction == 'Sud' :
            self.y -= 1
        elif self.direction == 'Ouest' :
            self.x -= 1
        elif self.direction == 'Nord' :
            self.y += 1
        elif self.direction == 'Est' :
            self.x += 1

    def turn_right(self) :
        if self.direction == 'Sud' :
            self.direction = 'Ouest'
        elif self.direction == 'Ouest' :
            self.direction = 'Nord'
        elif self.direction == 'Nord' :
            self.direction = 'Est'
        elif self.direction == 'Est' :
            self.direction = 'Sud'

    def state(self) :
        self.__repr__ = f'Etat : Nom : {self.name}, Position : {self.x}, {self.y}, Direction : {self.direction}'
        print(self.__repr__)