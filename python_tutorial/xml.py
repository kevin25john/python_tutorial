'''from xml.sax import contenthandler,make_parser
import xml.sax
class Myhandler(contenthandler):
    def startElement(self,name,attribute):
        print("Start element: ",name)
    def Characters(self,chars):
        print(">",chars,"<")
    def StartDocument(self):
        print("start document")

filename = r"F:\python\helloworld.xml"
sax_parser = make_parser()
with open(filename) as f:
    xml.sax.parse(f,Myhandler())

'''


import untangle
import xmltodict
filename = r"F:\python\helloworld.xml"
obj = untangle.parse(filename)
myModelName = obj.root.child['name']
print(myModelName)