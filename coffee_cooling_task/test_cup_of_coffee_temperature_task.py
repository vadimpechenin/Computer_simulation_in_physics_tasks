"""CupOfCoffee Class testing program
Task from the book Computer modeling in physics
Gould H., Tobochek I.
"""

import unittest
from cupofcoffee import CupOfCoffee

class Test_CupOfCoffee(unittest.TestCase):
    def setUp(self):
        """Create a survey and answer set for test methods.
        """
        time_initial=0
        coffee_temperature_initial=83
        room_temp=22
        time_increment=1
        cooling_coefficient=0.1
        self.my_cupofcoffee = CupOfCoffee(time_initial, coffee_temperature_initial,
                                          room_temp, time_increment, cooling_coefficient)
        self.responses = [83, 76.9, 71.41, 66.47, 62.02, 58.02, 54.42, 51.18,
                          48.26, 45.63, 43.27, 41.14, 39.22, 37.51, 35.95, 34.56]
        self.delta=[]
        for i in range(len(self.responses)):
            self.delta.append(0.1)
    def test_coffee_cooling_one_value(self):
        """Checks a method against a single value"""
        self.my_cupofcoffee.coffee_cooling()
        self.assertIn(self.responses[1], self.my_cupofcoffee.temperature_list)

    def test_coffee_cooling_all_values(self):
        """Checks a method against a all values"""
        self.my_cupofcoffee.coffee_cooling()
        delta=[]
        for i in range(len(self.responses)):
            delta.append(abs(self.responses[i]-self.my_cupofcoffee.temperature_list[i]))
        self.assertLessEqual(delta,self.delta)

unittest.main()

