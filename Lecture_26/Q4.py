browsers = dict(Samsung=2.81, Chrome=64.67,
                Firefox=3.66, Safari=19.06,
                Opera=2.36, Edge=3.99,)
data = browsers.values()
print(sorted(data, reverse=True).pop())
