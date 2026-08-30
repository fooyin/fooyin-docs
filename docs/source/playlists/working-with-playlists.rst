Working with Playlists
======================

A playlist is an ordered collection of tracks. It can be used for a temporary
listening session, saved inside fooyin, or exported to a playlist file.

Creating and Selecting Playlists
--------------------------------

Choose ``File -> New playlist`` to create an empty playlist. Depending on the
layout, playlists can be selected using **Playlist Tabs**, a **Playlist
Switcher**, the **Playlist Organiser**, or the **Playlist Manager**.

``View -> Playlist Manager`` opens a separate manager even when the current
layout does not contain a playlist-management widget. It can activate, rename,
remove, and create playlists and autoplaylists.

The **current playlist** is the one displayed and targeted by commands such as
``File -> Add files``. It is not necessarily the playlist containing the playing
track. ``View -> Show playing track`` returns to the playlist and track currently
being played.

Adding Tracks
-------------

Tracks can be added to the current playlist by:

* Dragging files or folders from the system file manager.
* Choosing ``File -> Add files`` or ``File -> Add folders``.
* Dragging or sending a selection from a library widget.
* Loading an existing playlist file.
* Adding an ``http://`` or ``https://`` stream with ``File -> Add stream URL``.

Files added directly to a playlist do not become part of a configured library.
fooyin may retain enough information to play and display them, but they will
not appear in library browsers unless their folder is indexed.

Editing Playlist Contents
-------------------------

Select tracks in the playlist and use the Edit menu, keyboard shortcuts, drag
and drop, or the context menu to change the list. Common operations include:

* Cut, copy, and paste.
* Remove selected tracks or clear the playlist.
* **Crop**, which removes everything except the selection.
* Remove duplicate or unavailable entries.
* Drag tracks to a new position.
* Reverse, randomise, or sort selected tracks or the entire playlist.

Playlist edits have their own undo and redo history. Removing a track from a
playlist does not delete its audio file or remove it from the library.

Renaming, Reordering, and Removing Playlists
--------------------------------------------

Right-click a playlist tab to rename it, move it left or right, save it, or
remove it. The Playlist Manager and Playlist Organiser provide similar actions
and are more convenient for a large number of playlists. The organiser can
also create groups and sort playlists alphabetically.

When fooyin offers **Restore deleted playlist** in a playlist menu, select the
removed playlist there to restore it. Treat this as a convenience rather than
a substitute for exporting important playlists.

Saving and Loading Playlist Files
---------------------------------

``File -> Load playlist`` imports a supported playlist file as a fooyin
playlist. ``File -> Save playlist`` exports the current playlist, while
``File -> Save all playlists`` exports every playlist to a selected folder.

Settings under **Playlist > Saving** control whether paths are written
automatically, as absolute paths, or relative to the playlist file. Relative
paths are useful when the playlist and music will be moved together. Absolute
paths are unambiguous on the current computer but are less portable.

**Write metadata** includes supported track information in exported formats
that can carry it.

Automatic Export
----------------

The **Auto-export** settings under **Playlist > Saving** can synchronise
fooyin playlists to a chosen folder and format. Options determine what happens
to exported files when a playlist is deleted or becomes empty, including
moving it to trash or preserving its last state.

Use auto-export when another application or device reads playlist files from a
shared location.

Playlist Appearance
-------------------

The playlist context menu provides quick access to column layouts and playlist
presets. A playlist can follow the default view or use a custom layout of its
own.

Preferences under **Playlist > Columns**, **Playlist > Presets**, and
**Playlist > Appearance** control fields, grouping headers, artwork, row
height, colours, and other presentation details. Many text fields accept
FooScript; see :doc:`../scripting/basics`.

For playlists populated by a saved search, continue with
:doc:`autoplaylists`. For one-off control of upcoming playback, use
:doc:`playback-queue`.
