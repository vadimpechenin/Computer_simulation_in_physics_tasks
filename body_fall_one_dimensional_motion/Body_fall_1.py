"""One-dimensional motion of a falling ball
Class of the task
Task from the book Computer modeling in physics
Gould H., Tobochek I.
"""

import matplotlib.pyplot as plt
import math

class BallFallingInViscousMedium():
    """Class describing the free fall of a ball in a viscous medium"""
    def __init__(self, initial_height, starting_speed,  radius, viscosity=1480, body_density=7800, medium_density=1260, calculation_step=0.02):
        self.initial_height=initial_height
        self.starting_speed = starting_speed
        self.viscosity = viscosity
        self.body_density = body_density
        self.medium_density = medium_density
        self.radius = radius
        self.calculation_step = calculation_step
        self.height_list = [initial_height]
        self.speed_list = [starting_speed]

    def ball_falling(self):
        """Function simulating the free fall of a ball in a viscous environment"""

        ACCELERATION_OF_GRAVITY = 9.8

        def plot_a_solution(time_list, height_list, speed_list):
            """ Plot results of calculation"""
            fig = plt.figure()

            plt.subplot(2, 1, 1)
            plt.plot(time_list, height_list, linewidth=5)
            plt.xlabel("Time, sec", fontsize=14)
            plt.ylabel("Ball height, m", fontsize=14)
            plt.tick_params(axis='both', labelsize=14)

            plt.subplot(2, 1, 2)
            plt.plot(time_list, speed_list, linewidth=5)
            plt.xlabel("Time, sec", fontsize=14)
            plt.ylabel("Ball speed, m/sec", fontsize=14)
            plt.tick_params(axis='both', labelsize=14)

            plt.show()

        # total time in seconds
        total_time = 10
        time = 0
        height = self.initial_height
        speed = self.starting_speed
        #lists for saving data
        time_list=[time]
        # We calculate the total number of steps
        ncalc=(total_time)/self.calculation_step
        mass_of_ball=4/3*math.pi*self.radius**3*self.body_density
        medium_resistance_coefficient=6*math.pi*self.viscosity*self.radius
        reduced_mass = 4/3*math.pi*(self.body_density-self.medium_density)*(self.radius**3)
        for step in range(int(ncalc)):
            speed=speed+self.calculation_step/2*((reduced_mass*ACCELERATION_OF_GRAVITY-medium_resistance_coefficient*speed)/
                                            mass_of_ball+(reduced_mass*ACCELERATION_OF_GRAVITY-
                                            medium_resistance_coefficient*(speed+self.calculation_step*
                                            (reduced_mass*ACCELERATION_OF_GRAVITY-medium_resistance_coefficient*speed)/
                                                                           mass_of_ball))/mass_of_ball)
            height = height + speed * self.calculation_step
            time = time + self.calculation_step
            time_list.append(time)
            self.height_list.append(height)
            self.speed_list.append(speed)

        plot_a_solution(time_list, self.height_list, self.speed_list)



