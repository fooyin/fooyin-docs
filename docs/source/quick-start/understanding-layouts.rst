Understanding Layouts
=====================

A layout is a tree of widgets and containers.
Understanding this hierarchy makes the layout-editing context menu much easier to use.

Widgets and Containers
----------------------

A **widget** provides a feature, such as a playlist, library tree, seek bar, or artwork display.

A **container** holds other widgets. The most important containers are:

* **Splitter (Left/Right)**, which arranges its children horizontally.
* **Splitter (Top/Bottom)**, which arranges its children vertically.
* **Tab Stack**, which places multiple children on separate tabs in the same area.

A splitter can contain ordinary widgets or other containers.
Nested splitters are how more complex rows and columns are constructed.

For example, a layout could have this structure::

   Splitter (Top/Bottom)
   +-- Splitter (Left/Right)
   |   +-- Library Tree
   |   +-- Artwork
   +-- Playlist

The top-level splitter creates two rows. Its first child creates two columns within the upper row.

The Selected Widget and Its Parents
-----------------------------------

In Layout Editing Mode, right-clicking selects the widget under the pointer.
fooyin highlights its region and builds a context menu for that widget.
The menu may then include sections headed ``Parent: ...`` for one or more containers above it.

Actions in the first section affect the selected widget. Actions in a parent section affect the surrounding container.
Check the section heading before choosing **Replace**, **Split**, **Move**, or **Remove**.

Empty Areas
-----------

Removing a widget can leave an empty placeholder. Right-click the placeholder and use **Insert** to choose a new widget.
Empty placeholders do not show parent sections in their editing menu.

Layout Contents and Appearance
------------------------------

A layout always stores its widget hierarchy and widget settings.
It can also be configured to restore a theme or window size when selected.
These optional properties are described in :doc:`managing-layouts`.

Continue with :doc:`layout-editing-mode` for a practical editing walkthrough.
