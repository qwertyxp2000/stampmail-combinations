#Your two "stamps": "a" and "b"
a = 6
b = 9

#"num" for the number to divide integerly into
num = 54
#"result" for result stuffs
result_a = 0
result_b = 0

#list of 'a' and 'b' workable combos
list_a = []
list_b = []

#AIM: Your aim is to find the stampmail combination for each of these stamps.
#print result with num/a
result_a = num/a
print("Testing dividing by all 'a': %s" % (result_a))
result_a_integeronly = num//a
print("Divisor only for 'a': %s" % (result_a_integeronly))

if ((num % a) == 0):
    print("int with 'a', so yes it works!")
else:
    print("nope.avi")

#print result with num/b
result_b = num/b
print("Testing dividing by all 'b': %s" % (result_b))
result_b_integeronly = num//b
print("Divisor only for 'b': %s" % (result_b_integeronly))

if ((num % b) == 0):
    print("int with 'b', so yes it works!")
else:
    print("nope.avi")

print("------------------------------")

#Do the 'a' then 'b' combos
for i in range(0, result_a_integeronly + 1): #start from zero, go up to result_a_integeronly as the final inclusive
    print("")
    result = num - i * a
    print("Result left with %sth value of 'a': %s" % (i, result))
    result_int = result // b #get an int-only with no remainder
    result /= b
    print("Result after dividing by 'b': %s" % (result))

    if ((result % 1) == 0):
        print("int with 'a', so now go add to list for 'a' and 'b'")
        list_a.append(i)
        list_b.append(result_int)
    else:
        print("nope.avi")

#print those results of list_a and list_b combos
print(list_a)
print(list_b)

#btw, some random bs about coding...
#If instance is float: https://bobbyhadz.com/blog/python-check-if-number-is-int-or-float
