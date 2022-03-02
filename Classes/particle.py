""" Creating  a class particle """


class Particle(object):

    """ Attribute that belongs to all particle objects """

    roar = 'I am a particle!'

    def __init__(self, charge, mass, position):

        """ Initialises particle with supplied values for charge, mass and position """
        self.c = charge
        self.m = mass
        self.p = position

    def hear_me(self):
        myroar = self.roar + (
            " My charge is:   " + str(self.c) +
            " My position is:   " + str(self.p) +
            " My mass is:   " + str(self.m)
        )
        print(myroar)
