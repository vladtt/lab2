def chil (arr):
    for emp in arr:
        for child in emp ["children"]:
            if child["age"]>18:
                print (emp["name"])
                break

ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
   }],
}

emps = [ivan, darja]

chil (emps)