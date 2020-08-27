def po():
    print(123)

o = {
    "w": po,
}

p = {
    "q": 2
}
q = list(p)
# q = dict(o.items() + p.items())
o["w"]()
