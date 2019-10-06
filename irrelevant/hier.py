"""
Options for struture of trees
  1) Preserving a hierarchy, at which we only know our ancestors at the time of ancestoring
  2) "Here is a hierarchy, we don't know what else exists"

All benefit from a "create ['animal', 'mammal', 'dog', 'alsatian']" strategy.
"""

from ricecooker.classes.nodes import TopicNode

topic_index = {} # hierarchical dictionaries

def get_topic(hier, channel):
    for i, cat_name in enumerate(hier):
        so_far = tuple(hier[:i+1])
        next_node = topic_index.get(so_far, None)
        if next_node:
            continue
        topic_index[so_far] = TopicNode(source_id=str(so_far), title=cat_name)
        parent_index = so_far[:-1] 
        if parent_index:
            parent = topic_index[parent_index]
        else:
            parent = channel
        parent.add_child(topic_index[so_far])
    return topic_index[so_far]

root = TopicNode("root", "root")
get_topic(["cat", "dog", "elf"], root)
get_topic(["cat", "dog", "dwarf"], root)

print (topic_index)

        