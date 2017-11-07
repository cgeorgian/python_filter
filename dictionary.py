from collections import defaultdict

class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


hits = defaultdict(list)

# hits = {"home": 100,
#         "sitemap": 27,
#         "about": 43}
hits['home'].append(1)
hits['site'].append(2)
hits['home'].append(4)
# hits['about'] = 130
# hits['home'] = 99
# hits['home'] = 12
# hits['site'] = 100


keys = hits.keys()
values = hits.values()

print("Keys:")
print(keys)
print(len(keys))

print("Values:")
print(values)
print(len(values))
