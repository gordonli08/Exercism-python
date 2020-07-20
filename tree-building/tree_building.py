class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if len(records) == 0:
        return None
    records.sort(key= lambda x: x.record_id)

    if records[0].parent_id != 0:
        raise ValueError("Root cannot have a parent")

    for i,r in enumerate(records):
        if r.parent_id >= r.record_id and r.record_id != 0:
            raise ValueError("Parent ID must always be lower than its own ID and cannot be equal to itself (except root)")

        if i != r.record_id:
            raise ValueError("Record ID {} missing from list of records".format(i))

    trees = { records[0].record_id : Node(records[0].record_id) }

    for r in records[1:]:
        trees[r.record_id] = Node(r.record_id)
        if r.parent_id in trees.keys():
            trees[r.parent_id].children.append(trees[r.record_id])

    return trees[0]
