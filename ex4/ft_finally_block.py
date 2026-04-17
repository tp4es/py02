# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tide-oli <marvin@42.fr>                   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/17 00:32:56 by tide-oli        #+#    #+#               #
#  Updated: 2026/04/17 11:54:17 by tide-oli        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

#!/usr/bin/env python3

class	GardenError(Exception):
	pass
class PlantError (GardenError):
	def	__init__(self, msg="Default PlantError!!!"):
		self.msg = msg
		super().__init__(msg)
class WaterError (GardenError):
	def	__init__(self, msg="Default WaterError!!!"):
		self.msg = msg
		super().__init__(msg)


def	water_plant(plant_name):
	if plant_name != plant_name.capitalize():
		raise PlantError
	else:
		print(f"***  Successful watering of the plant: {plant_name}  ***")

def	test_watering_system():
	print("=== Starting Watering System ===")
	name_list = {"Tomato", "Lettuce", "Carrot", "invalid name", "Pumpkin"}
	try:
		for plant in name_list:
			water_plant(plant)
	except Exception as e:
		print(f"{e}")
		return
	finally:
		print("*** ¡Closing! ***")

def	ft_finally_block():
	test_watering_system()

if __name__ == "__main__":
	ft_finally_block()