from contextlib import contextmanager
from io import BytesIO, StringIO
from os.path import join as path_join
from pathlib import Path
from pkgutil import get_data
from tempfile import NamedTemporaryFile
from typing import IO, Any, Dict, Iterator, Type, TypeVar
from zipfile import ZipFile

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


def load_csv(path: Path, **kwargs: Any) -> DataFrame:
    with ZipFile(BytesIO(_load_resource(str(path.with_suffix(".csv.zip"))))) as zip_fh:
        with zip_fh.open(f"{path.name}.csv") as fh:
            return read_csv(StringIO(fh.read().decode("utf8")), **kwargs)


@contextmanager
def resource_as_binary_tempfile(path: str) -> Iterator[IO[bytes]]:
    content = _load_resource(path)
    with NamedTemporaryFile() as fh:
        fh.write(content)
        fh.seek(0)
        yield fh
