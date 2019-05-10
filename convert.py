import json
import xmltodict
import pprint

p = pprint.PrettyPrinter(indent=2)

with open("postman.jmx", "rb+") as fp:
    p.pprint(xmltodict.parse(fp))
