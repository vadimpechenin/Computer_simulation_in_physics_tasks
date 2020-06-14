import matplotlib.pyplot as plt

class CupOfCoffee():
    """Class describing a cup of coffee"""
    def __init__(self,time_initial, coffee_temperature_initial, room_temp, time_increment, cooling_coefficient):
        self.time_initial=time_initial
        self.coffee_temperature_initial=coffee_temperature_initial
        self.room_temp=room_temp
        self.time_increment=time_increment
        self.cooling_coefficient=cooling_coefficient
        self.temperature_list = [coffee_temperature_initial]

    def coffee_cooling(self):
        """The function simulating the cooling of coffee according to the Euler method"""

        def plot_a_solution(time_list, temperature_list):
            """ Plot results of calculation"""
            plt.plot(time_list, temperature_list, linewidth=5)
            plt.xlabel("Time, min", fontsize=14)
            plt.ylabel("Temperature of coffee, C", fontsize=14)
            plt.tick_params(axis='both', labelsize=14)
            plt.show()

        # total time in minutes
        total_time=15
        time=self.time_initial
        temperature=self.coffee_temperature_initial
        #lists for saving data
        time_list=[time]
        # We calculate the total number of steps
        ncalc=(total_time-self.time_initial)/self.time_increment
        for step in range(int(ncalc)):
            change=-self.cooling_coefficient*(temperature-self.room_temp)
            temperature = temperature + change * self.time_increment
            time = time + self.time_increment
            time_list.append(time)
            self.temperature_list.append(temperature)

        plot_a_solution(time_list,self.temperature_list)




