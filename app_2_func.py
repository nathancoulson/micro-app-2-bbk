import random
import math

def list_gen_count(num):
    num_list = []

    for i in range(num*5):
        num_list.append(random.randint(num, num*5))

    length = len(num_list)

    num_list.sort()

    num_count = num_list.count(num)

    return num_list[num]

def recon_path(app_list):
	path = ""
	length = len(app_list)
	for app in app_list:
		if length > 1:
			path += str(app) + "-"
		else:
			path += str(app)
		length -= 1
	return path
