f = open('../data/RNA_intro/gene_expression.txt')
a = f.readlines()
f.close()
# print(a)
data = []

for i in range(len(a)):
	t = a[i][:len(a[i])-1].split('\t')
	t = (t[0], int(t[1]), int(t[2]))
	if t[1] + t[2] >= 15:
		data.append(t)

# print(data)
metrics = []

for i in data:
	metrics.append((i[0],(i[1]-i[2])/(i[1]+i[2])))

sorted_arr = sorted(metrics, key = lambda x: float(x[1]))

# print(metrics, sorted_arr)
print(len(sorted_arr))
print('\n\n\n', sorted_arr[:50])
print('\n\n\n', sorted_arr[len(sorted_arr)-50 : len(sorted_arr)])

