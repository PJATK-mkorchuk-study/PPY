#try:
#    file = open("my_file.txt", "tw")
#    file.write("something")
#except:
#    print("error")
#finally:
#    file.close()


#with open("my_file.txt", "tw") as file:
#    file.write("something2")
#    file.writelines(["some", "other", "lines"])


#with open("my_file.txt", "tr") as file:
#    data = file.read(2)
#    print(data)
#
#    while data := file.readline():
#        print(data)


import re

txt = "Some text with Capitalized Letters"

o = re.search("[A-Z]\\w*", txt)
print(o.group())

o = re.findall("[A-Z]\\w*", txt)
print(o)

o = re.split("\\s+", txt)
print(o)

o = re.sub("[Aa]", "@", txt)
print(o)
