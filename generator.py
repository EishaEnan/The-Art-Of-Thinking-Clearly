#Generates a connections Set using references for each chapter from the raw_data module

def connector(chapters):
    connections = set()

    for i, chapter in enumerate(chapters):
        for ref in chapter[1]:
            if (i, ref-1) not in connections or (ref-1, i) not in connections:
                connections.add((i, ref-1))
    return connections
