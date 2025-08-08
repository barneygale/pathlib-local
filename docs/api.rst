API Reference
=============


.. module:: pathlib_local


Classes
-------

.. class:: JoinableLocalPath

   Local path without I/O support. These objects are hashable and comparable.
   A string path can be retrieved by calling ``pathlib_abc.vfspath()``.

   .. attribute:: parser

      Always ``os.path``.

   .. attribute:: parts

      Tuple of path components.

   .. attribute:: anchor

      The path's irreducible prefix.

   .. attribute:: parent

      The path's lexical parent.

   .. attribute:: parents

      Sequence of the path's lexical parents, beginning with the immediate
      parent.

   .. attribute:: name

      The path's base name. The name is empty if the path has only an anchor,
      or ends with a slash.

   .. attribute:: stem

      The path's base name with the file extension omitted.

   .. attribute:: suffix

      The path's file extension.

   .. attribute:: suffixes

      Sequence of the path's file extensions.

   .. method:: with_name(name)

      Return a new path with a different :attr:`name`. The name may be empty.

   .. method:: with_stem(stem)

      Return a new path with a different :attr:`stem`, similarly to
      :meth:`with_name`.

   .. method:: with_suffix(suffix)

      Return a new path with a different :attr:`suffix`, similarly to
      :meth:`with_name`.

   .. method:: with_segments(*pathsegments)

      Create a new path object of the same type by combining the given
      *pathsegments*.

   .. method:: joinpath(*pathsegments)

      Return a new path with the given path segments joined onto the end.

   .. method:: full_match(pattern)

      Return true if the path matches the given glob-style pattern, false
      otherwise.


.. class:: ReadableLocalPath

   Path with support for reading data. This is a subclass of
   :class:`JoinableLocalPath`. These objects can be opened for reading with
   ``pathlib_abc.vfsopen()``.

   .. attribute:: info

      :class:`LocalPathInfo` object that supports querying the file type.

   .. method:: iterdir()

      Yield path objects for the directory contents.

   .. method:: readlink()

      Return the symlink target as a new path object.

   .. method:: read_bytes()

      Return the binary contents of the path.

   .. method:: read_text(encoding=None, errors=None, newline=None)

      Return the text contents of the path.

   .. method:: copy(target, **kwargs)

      Copy the path to the given target.

   .. method:: copy_into(target_dir, **kwargs)

      Copy the path *into* the given target directory. See :meth:`copy`.

   .. method:: glob(pattern, *, recurse_symlinks=True)

      Yield path objects in the file tree that match the given glob-style
      pattern.

      .. warning::

         For performance reasons, the default value for *recurse_symlinks* is
         ``True`` in this class, but for historical reasons, the default is
         ``False`` in ``pathlib.Path``. Furthermore, ``True`` is the *only*
         acceptable value for *recurse_symlinks* in this class.

         For maximum compatibility, users should supply
         ``recurse_symlinks=True`` explicitly when globbing recursively.

   .. method:: walk(top_down=True, on_error=None, follow_symlinks=False)

      Yield a ``(dirpath, dirnames, filenames)`` triplet for each directory
      in the file tree, like ``os.walk()``.


.. class:: WritableLocalPath

   Path with support for writing data. This is a subclass of
   :class:`JoinableLocalPath`. These objects can be opened for writing with
   ``pathlib_abc.vfsopen()``.

   .. method:: mkdir()

      Create this path as a directory.

   .. method:: symlink_to(target, target_is_directory=False)

      Create this path as a symlink to the given target.

   .. method:: write_bytes(data)

      Write the given binary data to the path, and return the number of bytes
      written.

   .. method:: write_text(data, encoding=None, errors=None, newline=None)

      Write the given text data to the path, and return the number of bytes
      written.


.. class:: LocalPath

    Path with support for reading and writing data. This is a subclass of
    :class:`ReadableLocalPath` and :class:`WritableLocalPath` with no further
    methods.


.. class:: LocalPathInfo

   Provides file type info. An instance of this class is provided by
   :attr:`ReadableLocalPath.info`.

   .. method:: exists(*, follow_symlinks=True)

      Return ``True`` if the path is an existing file or directory, or any
      other kind of file; return ``False`` if the path doesn't exist.

      If *follow_symlinks* is ``False``, return ``True`` for symlinks without
      checking if their targets exist.

   .. method:: is_dir(*, follow_symlinks=True)

      Return ``True`` if the path is a directory, or a symbolic link pointing
      to a directory; return ``False`` if the path is (or points to) any other
      kind of file, or if it doesn't exist.

      If *follow_symlinks* is ``False``, return ``True`` only if the path
      is a directory (without following symlinks); return ``False`` if the
      path is any other kind of file, or if it doesn't exist.

   .. method:: is_file(*, follow_symlinks=True)

      Return ``True`` if the path is a file, or a symbolic link pointing to
      a file; return ``False`` if the path is (or points to) a directory or
      other non-file, or if it doesn't exist.

      If *follow_symlinks* is ``False``, return ``True`` only if the path
      is a file (without following symlinks); return ``False`` if the path
      is a directory or other other non-file, or if it doesn't exist.

   .. method:: is_symlink()

      Return ``True`` if the path is a symbolic link (even if broken); return
      ``False`` if the path is a directory or any kind of file, or if it
      doesn't exist.
