#1
lst = [2, {}, 2.3, "abc", (4,), 2+2j]
res = [type(v).__name__ for v in lst]
print(res)

#2
lst = [[1, 11], [7, -3, 2], [5, 12, -6]]
res2 = [val for sublst in lst for val in sublst if val >= 0 and val <= 10]
print(res2)

#3
lst = [-2, 9, 11, 7, 1, 12, 9]
res3 = [0 if(val <0) else 10 if(val > 10) else val for val in lst]
print(res3)

#4
lst = ["Eve", "Jane", "Eve", "Mary", "John", "Mary", "Eve", "John"]
res4 = {name: lst.count(name) for name in lst}
print(res4)

#5
lst = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[1, 1, 1, 2]
]

res5 = [[row[i] for row in lst] for i in range(len(lst[0]))]
print(res5)

#6
lst = [ 87, 102, 90, 117, 95 ]
res6 = ["green" if(v<100 )else "yellow" if(v >=100 and v <=115) else "red" for v in lst]
print(res6)

#7
lst = ["a.pdf", "b.c", "c.pdf", "d.java", "e.f.pdf", "g.c"]
res7 = {extension: [v for v in lst if v.endswith("." + extension)] for extension in {name.split('.')[-1] for name in lst}}
print(res7)

#8
lst = [[[1, 2], ["a"]], [[3, 4, 5], ["b"]]]
res8 = [v for upperlst in lst for sublst in upperlst for v in sublst]
print(res8)

