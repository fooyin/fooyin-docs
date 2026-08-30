Adding Files
============

Music can be added as part of an indexed library or directly to a playlist.
The best method depends on whether fooyin should manage the files afterwards.

Adding a Library
----------------

A library is the recommended way to manage a permanent music collection.
Library tracks are indexed for browsing and searching and can be shown in library viewer widgets.

To add a library:

1. Choose ``Library -> Configure``.
2. Add a row to the library table and choose the folder containing your music.
3. Edit the generated library name if necessary.
4. Select **OK** or **Apply** to begin scanning.

Each library has a name and a root folder. Removing a library entry removes it
from fooyin's library database; it does not delete the audio files from disk.

.. image:: img/add-library.webp

Scanning and Monitoring
-----------------------

The initial scan finds supported files below the library folder and reads their metadata.
Progress is displayed in the main window in the status bar widget, where an active scan can also be cancelled.

The **Scanning** options on **Library > General** control how libraries are kept up to date:

* **Auto refresh on startup** checks libraries for changes when fooyin starts.
* **Monitor library directories** watches for files being added or removed.
* **Monitor track files** watches individual files for metadata changes. This option is available when directory monitoring is enabled.

Use ``Library -> Scan for changes`` to update files that have changed on disk.
Use ``Library -> Reload tracks`` when metadata should be read again for every track. Reloading the entire library takes longer.

The **Restrict to** and **Exclude** fields accept semicolon-separated file extensions, such as ``mp3;m4a``.
Leave **Restrict to** empty to use all supported types.

Adding Individual Files or Folders
----------------------------------

Use one of the following methods to add music directly to the current playlist:

* Drag files or folders onto a playlist widget.
* Choose ``File -> Add files``.
* Choose ``File -> Add folders``.

This is useful for occasional playback and for music stored outside your libraries.
The added tracks are not turned into a monitored library.

You can also choose ``File -> Add stream URL`` to add an ``http://`` or ``https://`` audio stream to the current playlist.

Library or Playlist?
--------------------

Use a **library** for a collection that you want to browse, search, and keep in sync.
Add files directly to a **playlist** when you only need them for playback or playlist organisation.

Continue with :doc:`../library/managing-library` for multiple libraries, unavailable tracks, and database maintenance.
See :doc:`../playlists/working-with-playlists` for playlist organisation and management.
