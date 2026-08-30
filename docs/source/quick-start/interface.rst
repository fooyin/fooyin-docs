Interface
=========

fooyin's main window is assembled from widgets. The visible widgets depend on the selected layout,
so two installations may look quite different while offering the same underlying features.

.. image:: img/interface.webp

Common Widget Roles
-------------------

Most layouts combine several of the following roles:

* **Library browsers** organise and filter music from indexed libraries.
* **Playlists** hold an ordered set of tracks for playback.
* **Player controls** provide play, pause, stop, and track navigation actions.
* **Seek bars** show playback progress and seek within the current track.
* **Volume controls** change the output volume.
* **Track information and artwork** show details for the playing or selected track.
* **Status widgets** show application state, including library scan progress.

Widgets can have their own context menus and configuration dialogs.
Their normal right-click menu is replaced by layout-editing actions while **Layout Editing Mode** is enabled.

Quick Setup
-----------

``View -> Quick setup`` provides the fastest way to change the overall layout, colour scheme, and playlist presentation.
It is useful both on first launch and when you want a different starting point for customisation.

Layouts
-------

A layout stores the widget arrangement and widget configuration.
Several built-in layouts are provided, and additional layouts can be created or imported.

Select a layout by name from the ``Layout`` menu. For more detail, continue with :doc:`understanding-layouts`
and :doc:`layout-editing-mode`.
