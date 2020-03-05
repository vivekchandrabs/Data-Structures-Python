# Usage: python rotation_array.py --rotation_constant 1 --direction right

import argparse

number_array = [1,2,3,4,5,6,7,8]


def array_rotation_function(array_to_be_rotated, direction, rotation_constant):
	for i in range((rotation_constant)):
		
		if direction == "left":
			temp = number_array.pop(0)
			array_to_be_rotated.append(temp)
		elif direction == "right":
			temp = number_array.pop()
			array_to_be_rotated.insert(0, temp)

	return array_to_be_rotated


if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("--rotation_constant", required=True)
	ap.add_argument("--direction", required=True)
	args = vars(ap.parse_args())

	output = array_rotation_function(number_array, args["direction"], int(args["rotation_constant"]))
	print(output)

