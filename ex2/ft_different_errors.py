# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tide-oli <marvin@42.fr>                   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/16 20:50:32 by tide-oli        #+#    #+#               #
#  Updated: 2026/04/16 22:53:14 by tide-oli        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

#!/usr/bin/env python3

def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("file.txt")
    elif operation_number == 3:
        "abc" + 5
    else:
        return

def	test_error_types():
   for i in range(5):
      print(f"Trying operation {i}")
      try:
         garden_operations(i)
      except ValueError as e:
              print(f"Caught ValueError: {e}\n")
      except ZeroDivisionError as e:
              print(f"Caught ZeroDivisionError: {e}\n")
      except FileNotFoundError as e:
              print(f"Caught FileNotFoundError: {e}\n")
      except TypeError as e:
               print(f"Caught TypeError: {e}\n")
      else:
              print("No error.\n")
   print("Program still running...")

def	ft_different_errors():
	test_error_types()

if __name__ == "__main__":
	ft_different_errors()