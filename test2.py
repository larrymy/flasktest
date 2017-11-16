# supplier = ["Mr Rice Corner", "Pontian Noodle", "Meet Mee", "Lim Fried Chicken"]
# supplier2 = [element.lower() for element in supplier]


# datacategory = ["Mr Rice Corner foo", "pontian noodle foobar", "bar lim fried chicken", "pontian noodle, cake"]
# datacategory = [element.lower() for element in datacategory]

# for p, q in enumerate(supplier):
# 	for i,x in enumerate(datacategory):
# 		if supplier2[p] in x:
# 			datacategory[i] = supplier[p]

# print(datacategory)


# 	indices = [i for i,x in enumerate(datacategory) if supplier2[p] in x]
# 	datacategory[indices] = supplier[p]


# indices = [i for i,x in enumerate(xs) if 'foo' in x]



def most_common(lst):
    return max(set(lst), key=lst.count)


x = ["a","b","c","a","a","bb"]

print(most_common(x))