Browsing the Library
====================

Once music has been indexed, library widgets provide structured browsing while search tools find tracks across
the whole collection. The widgets available in the main window depend on the current layout.

The Library Tree
----------------

The **Library Tree** groups tracks into a hierarchy. A grouping determines the fields and levels used to build that
hierarchy. Typical groupings organise by artist and album, genre, year, or folder.

Right-click the Library Tree header and open **Grouping** to switch grouping. Choose **Manage groupings** to create
or edit group definitions. Groupings can use FooScript, allowing library organisation to follow the metadata conventions
of your collection.

.. image:: img/library-tree-grouping.webp

In a folder-based grouping, the context menu can open the selected folder in the system file manager.

Playing and Sending Selections
------------------------------

A Library Tree selection may represent one track or an entire branch. The available context actions operate on all
tracks below the selection.

Common actions include:

* **Play**, which begins playback from the selected tracks.
* Sending or adding tracks to a playlist.
* **Add to playback queue**, which appends the tracks to the queue.
* **Queue to play next**, which places them at the front of the queue.
* **Remove from playback queue**, when matching tracks are already queued.

See :doc:`../playlists/working-with-playlists` for persistent organisation and :doc:`../playlists/playback-queue`
for temporary playback ordering.

Searching the Collection
------------------------

fooyin offers several routes into the same indexed collection:

* ``Library -> Search`` opens a full library search.
* ``Library -> Quick Search`` opens a temporary search popup.
* A **Search Bar** embedded in the layout provides persistent access.
* ``Library -> Show Recently Played`` and **Show Recently Added** run useful
  date-based searches.

Simple text is sufficient for ordinary searches. Advanced queries can compare metadata, combine conditions,
sort results, and limit the number of matches.
See :doc:`searching-library` for the query language.

Choosing Between Browsing and Searching
---------------------------------------

Use a library browser when you know where an item belongs in the collection or want to explore related albums
and artists. Use search when you know part of a name, want to combine metadata conditions,
or need a reusable dynamic result.

For a result that should remain available and update automatically, create an :doc:`../playlists/autoplaylists`
instead of repeatedly entering the same query.

If Tracks Do Not Appear
-----------------------

Check the following:

1. Confirm that the correct folder is listed under ``Library -> Configure``.
2. Run ``Library -> Scan for changes`` and wait for it to finish.
3. Review the **Restrict to** and **Exclude** extension lists.
4. Try ``Library -> Search`` to distinguish a grouping problem from a missing library record.
5. If the track exists in search but not the tree, switch grouping or inspect the metadata fields used by that grouping.

For disconnected storage or moved files, see the unavailable-track guidance in :doc:`managing-library`.
