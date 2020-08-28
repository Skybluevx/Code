
o = {}
def po():
    print(123)

def di():
    global o
    o["w"] = po


p = {
    "q": 2
}
q = list(p)
# q = dict(o.items() + p.items())
di()
o["w"]()
