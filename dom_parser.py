from xml.dom import minidom
from collections import defaultdict

doc = minidom.parse('static_analysis.xml')

flaws = doc.getElementsByTagName("flaw")
print len(flaws)

flaws2fix = defaultdict(list)
for flaw in flaws:
    severity = flaw.getAttribute("severity")
    source = flaw.getAttribute("sourcefile")
    scope = flaw.getAttribute("scope")
    line = flaw.getAttribute("line")
    flaws2fix[scope].append(int(line))
    print scope + ":" + source + ":" + line

keys = flaws2fix.keys()
values = flaws2fix.values()

for key in keys:
    print key
    print flaws2fix[key] + "\n"

# print("Keys:")
# print(keys)
#
# print("Values:")
# print(values)
