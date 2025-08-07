=============
pathlib-local
=============

|pypi| |docs|

This is an alternative implementation of the ``pathlib.PurePath`` and
``Path`` classes. It requires Python 3.9+. Four classes are provided:

1. ``JoinableLocalPath``, which is similar to ``pathlib.PurePath``
2. ``ReadableLocalPath``, which subclasses ``JoinableLocalPath``
3. ``WritableLocalPath``, which also subclasses ``JoinableLocalPath``
4. ``LocalPath``, which is similar to ``pathlib.Path`` and subclasses
   both ``ReadableLocalPath`` and ``WritableLocalPath``.

This package implements methods required by the ``pathlib-abc`` PyPI package,
and for comparisons and hashing, but not other ``pathlib.Path`` methods.
Please open an issue or PR if you'd like to see a method added. Certain
features (like ``LocalPath.info``, ``copy()`` and ``walk()``) are available
here but not in older versions of ``pathlib`` in the Python standard library.

Paths are not normalized, so leading ``./`` segments and trailing slashes are
retained.

.. |pypi| image:: https://img.shields.io/pypi/v/pathlib-local.svg
    :target: https://pypi.python.org/pypi/pathlib-local
    :alt: Latest version released on PyPi

.. |docs| image:: https://readthedocs.org/projects/pathlib-local/badge
    :target: http://pathlib-local.readthedocs.io/en/latest
    :alt: Documentation
