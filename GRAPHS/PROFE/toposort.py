from collections import deque


def toposortVisit(data, u):
    data["state"][u] = "VISITED"
    data["time"] = data["time"] + 1
    data["d"][u] = data["time"]
    for adj in data["g"][u]:
        if data["state"][adj] == "NOT_VISITED":
            data["parent"][adj] = u
            toposortVisit(data, adj)
    data["state"][u] = "FINISH"
    data["time"] = data["time"] + 1
    data["f"][u] = data["time"]
    data["list"].appendleft(u)


def toposort(g):
    data = {
        "g": g,
        "state": dict(),
        "parent": dict(),
        "d": dict(),
        "time": 0,
        "f": dict(),
        "list": deque()
    }
    for k in g.keys():
        data["state"][k] = "NOT_VISITED"
        data["parent"][k] = None
        data["d"][k] = 0
        data["f"][k] = 0
    for k in g.keys():
        if data["state"][k] == "NOT_VISITED":
            toposortVisit(data, k)

    return data['list']


# En el cero se mete una lista vacia para ignorar la posicion
g = {
    "calcetines": ["zapatos"],
    "pantalon": ["zapatos", "cinturon"],
    "camisa": ["cinturon", "jersey"],
    "zapatos": [],
    "cinturon": [],
    "jersey": []
}

print(toposort(g))
