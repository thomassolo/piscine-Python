def NULL_not_found(object : any) -> int:
    if object is None:
        print("Nothing:", object, type(object))
    elif type(object) == float:
        print("Cheese:", object, type(object))
    elif type(object) == int and object == 0:
        print("Zero:", object, type(object))
    elif type(object) == str and object == '':
        print("Empty:", object, type(object))
    elif type(object) == bool:
        print("Fake:", object, type(object))
    else:
        print("Type not found")
    return 1
    
        