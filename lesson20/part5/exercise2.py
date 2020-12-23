from graph import Graph
from lesson17.part11.exercise12.queue import Queue


def breadth_first_search(graph, start, finish):
    q = Queue()
    discovered = [start]
    q.enqueue(start)
    parent = {}
    while len(q) > 0:
        v = q.dequeue()
        if v == finish:
            break
        for neighbor in graph.neighbors(v):
            if neighbor.descr not in discovered:
                discovered += [neighbor.descr]
                parent[neighbor.descr] = v
                q.enqueue(neighbor.descr)
    path = [finish]
    while path[0] != start:
        path = [parent[path[0]]] + path

    print(path)


def main():
    facebook_users = Graph()
    for user in ["Bob", "Anne", "Elisa", "Diana", "Carl"]:
        facebook_users.add_vertex(user)

    # Carl's edges
    facebook_users.add_edge("Carl", "Bob")
    facebook_users.add_edge("Carl", "Elisa")
    facebook_users.add_edge("Carl", "Diana")

    # Diana's edges(+from previous edge additions)
    facebook_users.add_edge("Diana", "Bob")
    facebook_users.add_edge("Diana", "Anne")

    # Elisa's edges(+from previous edge additions)
    facebook_users.add_edge("Elisa", "Anne")

    # Anne's edges(+from previous edge additions)
    facebook_users.add_edge("Anne", "Bob")

    # Bob's edges (+from previous edge additions)

    # Print the graph
    print(facebook_users)
    print("\n")
    breadth_first_search(facebook_users, "Carl", "Anne")


main()
