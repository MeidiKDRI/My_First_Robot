# Creation of a new class for New Generation Robot
# THis new one is based on the first generation with more features.
from robot import Robot

class RobotNG(Robot) :

    def __init__(self, name) :
        super().__init__(name)
        self.turbo = 'Turbo Off'

    def boost(self) :
        if self.turbo == 'Turbo Off' :
            self.turbo = 'Turbo On'
        else :
            self.turbo = 'Turbo Off'
        return self.turbo

    def forward(self, nb_pace) :
        self.nb_pace = nb_pace

        if self.turbo == False :
            for i in range(self.nb_pace) :
                Robot.forward(self)
        else :
            for i in range(self.nb_pace * 3) :
                Robot.forward(self)

    def turn_left(self) :
        if self.direction == 'Ouest':
            self.direction = 'Sud'
        elif self.direction == 'Nord' :
            self.direction = 'Ouest'
        elif self.direction == 'Est' :
            self.direction = 'Nord'
        elif self.direction == 'Sud' :
            self.direction = 'Est'
        print(f'{self.name} a tourné vers {self.direction}')

    def turn_around(self) :
        if self.direction == 'Ouest':
            self.direction = 'Est'
        elif self.direction == 'Nord' :
            self.direction = 'Sud'
        elif self.direction == 'Est' :
            self.direction = 'Ouest'
        elif self.direction == 'Sud' :
            self.direction = 'Nord'
        print(f'{self.name} a tourné vers {self.direction}')

    def state(self) :
        Robot.state(self)
        print(self.turbo)
