students = {
     "sophs":  ["Tom", "Ann", "Bill", "Kim", "Jim"],
     "junior":  ["Lisa", "Stacey", "Mike", "Greg", "Tim"],
     "seniors":  ["Will", "Lyn", "Sue", "Janice", "Betty"]
       }

for key in students.keys():
    for name in students[key]:
        if "a" in name.lower():
            print(name)
