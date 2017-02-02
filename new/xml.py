import untangle
import xmltodict
filename = r"F:\python\helloworld.xml"
obj = untangle.parse(filename)
myModelName = obj.root.child['name']
print(myModelName)

'''import xmltodict
doc=xmltodict.parse("""<mydocument has = "an attribute"><and><many>eLements</many><many>more element</many></and><plusa="complex"> element aswell</plus></mydocument>""")

myvar1 = doc["mydocument"]["@has"]
myvar2 = doc ["mydocument"]["plus"]["@a"]
myvar3 = doc ["myydocument"]["plus"]["#text"]'''