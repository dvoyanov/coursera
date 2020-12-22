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


class AbstractLevel(yaml.YAMLObject):

    @classmethod
    def from_yaml(cls, loader, node):

        def get_map(loader, node):
            print("get_map_from_yaml")

        def get_objects(loader, node):
            print("get_object_from_yaml")

        loader.add_constructor(u'!easy_level', get_map)
        loader.add_constructor(u'!medium_level', get_map)
        loader.add_constructor(u'!hard_level', get_map)

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

tmp = yaml.load(yaml_MD)
print(tmp)