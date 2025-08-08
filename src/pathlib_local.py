import os
from urllib.request import pathname2url, url2pathname

from pathlib_abc import (
    PathInfo, JoinablePath, ReadablePath, WritablePath, vfspath)


__all__ = [
    'LocalPathInfo', 'JoinableLocalPath', 'ReadableLocalPath',
    'WritableLocalPath', 'LocalPath']
__version__ = '0.1.0'


class LocalPathInfo(PathInfo):
    __slots__ = ('_path', '_exists', '_is_dir', '_is_file', '_is_symlink')

    def __init__(self, path):
        self._path = path
        self._exists = None
        self._is_dir = None
        self._is_file = None
        self._is_symlink = None

    def exists(self, *, follow_symlinks=True):
        """Whether this path exists."""
        if not follow_symlinks and self.is_symlink():
            return True
        if self._exists is None:
            self._exists = os.path.exists(self._path)
        return self._exists

    def is_dir(self, *, follow_symlinks=True):
        """Whether this path is a directory."""
        if not follow_symlinks and self.is_symlink():
            return False
        if self._is_dir is None:
            self._is_dir = os.path.isdir(self._path)
        return self._is_dir

    def is_file(self, *, follow_symlinks=True):
        """Whether this path is a regular file."""
        if not follow_symlinks and self.is_symlink():
            return False
        if self._is_file is None:
            self._is_file = os.path.isfile(self._path)
        return self._is_file

    def is_symlink(self):
        """Whether this path is a symbolic link."""
        if self._is_symlink is None:
            self._is_symlink = os.path.islink(self._path)
        return self._is_symlink


class JoinableLocalPath(JoinablePath):
    __slots__ = ('_segments',)
    parser = os.path

    def __init__(self, *pathsegments):
        self._segments = pathsegments

    def __fspath__(self):
        return os.path.join(*self._segments) if self._segments else ''

    __vfspath__ = __fspath__

    def __repr__(self):
        return f'{type(self).__name__}({vfspath(self)!r})'

    @property
    def _str_normcase(self):
        # String with normalized case, for hashing and equality checks
        return os.path.normcase(vfspath(self))

    def __hash__(self):
        return hash(self._str_normcase)

    def __eq__(self, other):
        if not isinstance(other, JoinableLocalPath):
            return NotImplemented
        return self._str_normcase == other._str_normcase

    def __lt__(self, other):
        if not isinstance(other, JoinableLocalPath):
            return NotImplemented
        return self._str_normcase < other._str_normcase

    def __le__(self, other):
        if not isinstance(other, JoinableLocalPath):
            return NotImplemented
        return self._str_normcase <= other._str_normcase

    def __gt__(self, other):
        if not isinstance(other, JoinableLocalPath):
            return NotImplemented
        return self._str_normcase > other._str_normcase

    def __ge__(self, other):
        if not isinstance(other, JoinableLocalPath):
            return NotImplemented
        return self._str_normcase >= other._str_normcase

    def with_segments(self, *pathsegments):
        return type(self)(*pathsegments)

    def as_uri(self):
        """Return the path as a URI."""
        return 'file:' + pathname2url(vfspath(self))

    @classmethod
    def from_uri(cls, uri):
        """Return a new path from the given 'file' URI."""
        return cls(url2pathname(uri.removeprefix('file:')))


class ReadableLocalPath(JoinableLocalPath, ReadablePath):
    __slots__ = ('_info',)

    def __init__(self, *pathsegments):
        super().__init__(*pathsegments)
        self._info = LocalPathInfo(vfspath(self))

    @property
    def info(self):
        return self._info

    def __open_reader__(self):
        return open(vfspath(self), 'rb')

    def iterdir(self):
        return (self / name for name in os.listdir(vfspath(self)))

    def readlink(self):
        return self.with_segments(os.readlink(vfspath(self)))


class WritableLocalPath(JoinableLocalPath, WritablePath):
    def __open_writer__(self, mode):
        return open(vfspath(self), f'{mode}b')

    def mkdir(self):
        os.mkdir(vfspath(self))

    def symlink_to(self, target, target_is_directory=False):
        os.symlink(target, vfspath(self), target_is_directory)


class DeletableLocalPath(JoinableLocalPath):
    def rmdir(self):
        os.rmdir(vfspath(self))

    def unlink(self):
        os.unlink(vfspath(self))


class LocalPath(ReadableLocalPath, WritableLocalPath, DeletableLocalPath):
    pass
