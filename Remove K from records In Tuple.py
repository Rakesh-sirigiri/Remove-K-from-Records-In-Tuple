list = [(3,4,7), (9,2), (8,3), (7,4), (9,7, 2, 1)]
print("The original list is : " + str(list))
K = 7
res = [tuple(ele for ele in sub if ele != K) for sub in list]
print("The records after removing K : " + str(res))
