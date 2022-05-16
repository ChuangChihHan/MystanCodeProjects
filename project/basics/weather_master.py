"""
File: weather_master.py
Name: Maggie
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

EXIT = -100


def main():
	"""
	This program is used to find the maximum temperature, minimum temperature,average temperature,
	and the number of cold days according to the data the user inputs.
	"""
	print('stanCode "Weather Master 4.0" !')
	data = int(input("Next Temperature: (or -100 to quit)? "))
	cold_day = 0  # use to count the number of cold days
	if data == EXIT:  # for the condition that the user enters the exit number
		print("No temperatures were entered.")
	else:
		maximum = data  # place the value the user enter as a default value of max
		minimum = data  # place the value the user enter as a default value of min
		total_temp = data  # set the first data the user enter to calculate the sum of data
		number_of_temp = 1  # count the first data the user enter
		if data < 16:  # count the number of cold days
			cold_day += 1
		while True:
			data = int(input("Next Temperature: (or -100 to quit)? "))
			if data == EXIT:  # if enter exit number, break the while loop
				break
			else:
				if data < 16:
					cold_day += 1  # count the number of cold days
				number_of_temp += 1  # calculate how many data the user enter
				total_temp += data  # calculate the sum of data the user enter
				if data > maximum:  # if the following data the user enter is greater than the previous data
					maximum = data  # then the maximum will be the following data
				elif data < minimum:  # if the following data the user enter is less than the previous data
					minimum = data  # then the minimum will be the following data
		average = total_temp / number_of_temp  # calculate the average of the temperature
		print("Highest temperature = " + str(maximum))
		print("Lowest temperature = " + str(minimum))
		print("Average = " + str(average))
		print(str(cold_day) + " cold day(s)")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
