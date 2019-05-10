import json
import xmltodict
import pprint

p = pprint.PrettyPrinter(indent=2)

# with open("postman.jmx", "rb+") as fp:
#     p.pprint(xmltodict.parse(fp, dict_constructor=dict))

with open("test.json", "r") as fp:
    d = json.load(fp)
    d["root"] = "root"
    p.pprint(xmltodict.unparse(d, full_document=False, pretty=True))
