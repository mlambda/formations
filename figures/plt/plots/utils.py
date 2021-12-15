from typing import Dict, Type, TypeVar

_T = TypeVar("_T")
InstancesDict = Dict[Type[_T], _T]


class Singleton(type):

    _instances: InstancesDict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
