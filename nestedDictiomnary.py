myfamily = {
   
    "child1": {
        "name": "Sumon",
        "age": 23,
        "gender": "male"
    },
    "child2": {
        "name": "sumou",
        "age": 19,
        "gender": "female"
    }
}
print(myfamily["child2"]["name"])
myfamily["child1"]["age"]=25
print(myfamily)

child1 = {
    "name": "Aricu",
    "age": 25,
    "gender": "Male"
}

child2 = {
    "name": "usagi",
    "age": 20,
    "gender": "Famele"
}

my_dect={
    "child1":child1,
    "child2":child2
    }

print(my_dect)
child3={
    "name":"minhaj",
    "age":23,
    "gender":"m"
    }

my_dect["child3"]=child3
print(my_dect)
del my_dect["child1"]["age"]
print(my_dect)
my_dect["child1"]["age"]=78
print(my_dect)
