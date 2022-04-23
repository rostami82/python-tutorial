#            -7         -6        -5         -4        -3           -2         
#            0          1         2          3          4            5           
fruits = ["orange", "banana", "apricot", "cucumber","watermelon", "orange"]


# range index
# [start:end:step]
# [included: not included, step]

print(fruits[:1] + fruits[2:5:2])

print(fruits[1:2:1] + fruits[-3:-7:-3])

fruits.insert(2, "peach")
print(fruits)

fruits.remove("watermelon")
print(fruits)

fruits.extend(["cherry"])
print(fruits)

fruits[4] = "pineapple"
print(fruits)

fruits.remove("banana")
print(fruits)




