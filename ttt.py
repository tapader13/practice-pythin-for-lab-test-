my_dict= {
    "Brand": "ford" ,
    "model": "munstar",
    "year": 1999
    }

my_dict["modelda"]="jajaaj"


print(my_dict.pop("year"))
print(my_dict)
print(my_dict["model"])
print(my_dict.popitem())
del my_dict["Brand"]
print(my_dict)
    
