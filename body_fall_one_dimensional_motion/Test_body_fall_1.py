"""Test of class describing the free fall of a ball in a viscous medium
Task from the book Computer modeling in physics
Gould H., Tobochek I.
"""

import unittest
from Body_fall_1 import BallFallingInViscousMedium

class Test_BallFallingInViscousMedium(unittest.TestCase):
    def setUp(self):
        """Create a survey and answer set for test methods.
        """
        initial_height = 0
        starting_speed = 0
        radius=0.1
        self.my_ballfalling = BallFallingInViscousMedium(initial_height, starting_speed,  radius)
        self.responses = [[0, 0.024, 0.042, 0.0556, 0.0657, 0.0733, 0.079, 0.0833, 0.0866, 0.089, 0.0908, 0.0921],
                         [0, 0.00, 0.00, 0.00, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02]]
        self.responses = [0, 0.024, 0.042, 0.0556, 0.0657, 0.0733, 0.079, 0.0833, 0.0866, 0.089, 0.0908, 0.0921]

        self.delta = []
        for i in range(len(self.responses)):
            self.delta.append(0.001)
            
    def test_ballfalling_speed(self):
        """Checks a method against a heigth"""
        self.my_ballfalling.ball_falling()
        delta = []
        for i in range(len(self.responses)):
            delta.append(abs(self.responses[i] - self.my_ballfalling.speed_list[i]))
        self.assertLessEqual(delta, self.delta)

unittest.main()