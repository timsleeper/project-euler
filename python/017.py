import inflect

p = inflect.engine()
s = ""
for i in range(1, 1001):
    s = s + p.number_to_words(i)

s = s.replace(",","")
s = s.replace(" ","")
s = s.replace("-","")
print(len(s))