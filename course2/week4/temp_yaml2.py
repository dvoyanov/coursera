import yaml
from abc import ABC, abstractmethod

yaml_MD = '''
levels:
    - !easy_level {}
    - !medium_level
        enemy: ['rat']
    - !hard_level
        enemy:
            - rat
            - snake
            - dragon
        enemy_count: 10
'''


class AbstractLevel():

    @classmethod
    def get_map(cls):
        return cls.Map()

    @classmethod
    def get_objects(cls):
        return cls.Objects()

    class Map(ABC):
        pass

    class Objects(ABC):
        pass


class EasyLevel(AbstractLevel):
    yaml_tag = u'!easy_level'

    class Map:
        def __init__(self):
            print("init_easy_level_map")

        def get_map(self):
            print("get_easy_Level_Map")

    class Objects:
        def __init__(self):
            print("init_easy_level_object")

        def get_objects(self, _map):
            print("get_easy_Level_Object")


class MediumLevel(AbstractLevel):
    yaml_tag = u'!medium_level'

    class Map:
        def __init__(self):
            print("init_medium_level_map")

        def get_map(self):
            print("get_medium_Level_Map")

    class Objects:
        def __init__(self):
            print("init_medium_level_object")

        def get_objects(self, _map):
            print("get_medium_Level_Object")


class HardLevel(AbstractLevel):
    yaml_tag = u'!hard_level'

    class Map:
        def __init__(self):
            print("init_hard_level_map")

        def get_map(self):
            print("get_Hard_Level_Map")

    class Objects:
        def __init__(self):
            print("init_hard_level_object")

        def get_objects(self, _map):
            print("get_Hard_Level_Object")

def constructor_example_easy(loader, node):
    print("easy")
    print(loader.construct_mapping(node))
    return [1, ]

def constructor_example_medium(loader, node):
    print("medium")
    print(loader.construct_mapping(node))
    return [2, ]

def constructor_example_hard(loader, node):
    print("hard")
    print(node)
    value = loader.construct_scalar(node)
    value2 = yaml.serialize(node)
    print(value)

yaml.add_constructor(u'!easy_level', constructor_example_easy)
yaml.add_constructor(u'!medium_level', constructor_example_medium)
yaml.add_constructor(u'!hard_level', constructor_example_hard)
tmp = yaml.load(yaml_MD)
print(tmp)