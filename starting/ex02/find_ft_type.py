def all_thing_is_obj(object: any) -> int:
	if type(object) == list:
		print("List : ", type(object))
	elif type(object) == tuple:
		print("Tuple : ", type(object))
	elif type(object) == set:
		print("Set : ", type(object))
	elif type(object) == dict: 
		print("Dict : ", type(object))
	elif type(object) == str and object == "Brian":
		print("Brian is in the kitchen : ", type(object))
	elif type(object) == str and object == "Toto":
		print("Toto is in the kitchen : ", type(object))
	else:
		print("Type not found")
	return 42
