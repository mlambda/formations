from io import StringIO
from pkgutil import get_data
from typing import Any, Dict, Type, TypeVar

from pandas import DataFrame, read_csv

_T = TypeVar("_T")
InstancesDict = Dict[Type[_T], _T]


class Singleton(type):

    _instances: InstancesDict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


def load_csv(path: str, **kwargs: Any) -> DataFrame:
    content = get_data(__name__, path)
    if content is None:
        raise RuntimeError(f"Could not load {path}")
    df = read_csv(StringIO(content.decode("utf8")), index_col="Date", parse_dates=True)
    df = df.resample("90d").mean()
    return df
