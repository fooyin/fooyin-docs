Managing Your Library
=====================

A library is a named folder that fooyin indexes for browsing and searching.
It is intended for music that forms a permanent part of your collection.
For occasional playback without indexing a folder, see :doc:`../quick-start/adding-files`.

Adding and Editing Libraries
----------------------------

Choose ``Library -> Configure`` to open **Library > General**. The table at the
top of the page contains the configured libraries.

To add a library:

1. Add a row to the table.
2. Select the root folder containing the music.
3. Edit the generated name if necessary.
4. Select **Apply** or **OK**.

The folder name is used as the initial library name. A library can include
subfolders, so you normally only need to add the highest folder that belongs to
that collection.

You can configure multiple libraries. Giving them meaningful names makes it
easier to distinguish their tracks in library views and track information.

Removing a library entry removes its tracks from fooyin's library. It does not
delete the audio files from disk.

The Initial Scan
----------------

Applying a new library starts a scan. fooyin enumerates the folder, reads
metadata from supported files, and writes the resulting tracks to its library
database. Progress is shown in the status area of the main window.

The application remains usable during a scan. Use ``Library -> Cancel current
scan`` or the cancel control in the status area to stop an active scan. Tracks
from the previous library state remain available; scan again later to finish
updating the library.

Scan for Changes or Reload Tracks?
----------------------------------

``Library -> Scan for changes`` checks configured libraries and updates tracks
whose files have changed. Use it after adding, moving, retagging, or removing
files outside fooyin.

``Library -> Reload tracks`` reads metadata again for every track in every
library. It takes longer and is mainly useful when a broad external change was
not detected correctly.

You can also right-click a library on **Library > General** to scan or reload
only that library. An active per-library scan can be cancelled from the same
menu.

Automatic Updates
-----------------

The **Scanning** group on **Library > General** provides three related options:

* **Auto refresh on startup** scans libraries for changes when fooyin starts.
* **Monitor library directories** watches for files being added or removed while fooyin is running.
* **Monitor track files** watches individual audio files for tag changes.
  It is available when directory monitoring is enabled.

Monitoring reduces the need for manual scans, but a manual scan remains useful
after large file operations or changes made while fooyin was not running.
See :doc:`../files/file-operations` for moving library files from within
fooyin.

Restricting File Types
----------------------

The **File Types** group controls which supported files are included:

* **Restrict to** scans only the listed extensions.
* **Exclude** ignores the listed extensions.

Enter extensions without wildcards and separate them with semicolons, for
example ``flac;ogg;mp3``. Leave **Restrict to** empty to allow all supported
types. These settings apply to library scanning rather than files manually
added to a playlist.

Unavailable Tracks
------------------

A track becomes unavailable when its indexed file can no longer be accessed.
This can happen when a file is moved, a removable drive is disconnected, or a
network location is offline.

The **Availability** options can mark inaccessible tracks when fooyin starts or
when playback encounters them. Marking a track unavailable retains its library
record, which is useful when the storage may return later.

After reconnecting the storage or restoring the path, run **Scan for changes**.
Use ``Library -> Database -> Remove unavailable tracks`` only when the files are
not expected to return. This removes their records from the database and
libraries; it does not delete files from disk.

.. warning::

   Do not remove unavailable tracks merely because a removable or network
   library is temporarily disconnected.

Database Maintenance
--------------------

The ``Library -> Database`` menu contains maintenance actions:

* **Clean** removes non-library tracks that are no longer referenced by a playlist,
  together with expired playback statistics.
* **Optimise** reduces database size and improves query performance.
* **Remove unavailable tracks** removes unavailable records from the database and configured libraries.

Routine use does not require frequent database maintenance. **Clean** and
**Remove unavailable tracks** affect stored records, so review playlists and
unavailable storage before using them.

Metadata and Playback Statistics
--------------------------------

Settings under **Library > Metadata** control how fooyin handles compilations,
ratings, and play counts. Ratings and play counts are always usable in the
database; they can also be written to file tags when the format and file
permissions allow it.

The overwrite options determine whether values read from files replace the
database values when tracks are reloaded. Choose these according to which
application should be the authoritative source for ratings and play counts.
