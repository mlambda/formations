from contextlib import contextmanager
from io import StringIO
from os.path import join as path_join
from pkgutil import get_data
from tempfile import NamedTemporaryFile
from typing import IO, Any, Dict, Iterator, Type, TypeVar

from pandas import DataFrame, read_csv

_T = TypeVar("_T")
InstancesDict = Dict[Type[_T], _T]


class Singleton(type):

    _instances: InstancesDict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


def _load_resource(path: str) -> bytes:
    content = get_data(__name__, path_join("data", path))
    if content is None:
        raise RuntimeError(f"Could not load {path}")
    return content


def load_csv(path: str, **kwargs: Any) -> DataFrame:
    return read_csv(StringIO(_load_resource(path).decode("utf8")), **kwargs)


@contextmanager
def resource_as_binary_tempfile(path: str) -> Iterator[IO[bytes]]:
    content = _load_resource(path)
    with NamedTemporaryFile() as fh:
        fh.write(content)
        fh.seek(0)
        yield fh
