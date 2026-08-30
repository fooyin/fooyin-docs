Searching and Query Syntax
==========================

fooyin can search the library using ordinary text or structured queries. Plain
text is suitable when you know part of an artist, album, title, or another
searchable field. Queries are useful when you want to search a particular
field, compare values, combine conditions, sort results, or limit their number.

The same query syntax is available in the full library search, Quick Search,
Search Bar widgets, and autoplaylists.

Quick Examples
--------------

.. list-table::
   :widths: 45 55
   :header-rows: 1

   * - Find
     - Search
   * - Words in searchable metadata
     - ``radiohead moon``
   * - An exact phrase
     - ``"dark side of the moon"``
   * - Tracks by an artist
     - ``artist : radiohead``
   * - Tracks rated four stars or higher
     - ``rating >= 4``
   * - Tracks without lyrics
     - ``lyrics MISSING``
   * - Tracks added during the last two weeks
     - ``addedtime DURING LAST 2 WEEKS``
   * - Recent jazz tracks
     - ``genre = jazz AND addedtime DURING LAST MONTH``

Plain Text Searches
-------------------

A plain text search checks the fields configured under
``Edit -> Settings -> Library -> Searching -> General``. By default these
include the artist, title, album, album artist, performer, composer, genre,
comment, and file path.

All words must match, but they do not need to occur in the same field or order.
For example, ``radiohead bends`` can match an artist of "Radiohead" and an album
of "The Bends". Enclose text in double quotes when the complete phrase must
occur together:

``"wish you were here"``

Text matching ignores case and accents. The default search mode matches the
beginnings of words, so ``light`` matches "Light", but not "Moonlight". Change
**Search mode** to **Match anywhere** in the search settings if you want both to
match. These settings affect plain text searches, not field-based query
expressions.

Searching Fields
----------------

Use a field name followed by an operator and a value:

``artist : miles davis``

Field names can be written with or without percent signs, so ``artist`` and
``%artist%`` are equivalent in a query. Custom metadata fields can be searched
the same way. See :doc:`../scripting/variables` for the built-in fields.

String comparisons ignore case and accents. Use ``:`` to find a value anywhere
within a field and ``=`` to require the complete field value:

.. list-table::
   :widths: 18 27 35 20
   :header-rows: 1

   * - Operator
     - Syntax
     - Meaning
     - Keyword form
   * - ``:``
     - ``field : value``
     - Field contains the value
     - ``HAS``
   * - ``=``
     - ``field = value``
     - Field equals the value
     - ``IS``
   * - ``!=``
     - ``field != value``
     - Field does not equal the value
     - ``NOT =``
   * - ``>``
     - ``field > number``
     - Field is greater than the number
     - ``GREATER``
   * - ``<``
     - ``field < number``
     - Field is less than the number
     - ``LESS``
   * - ``>=``
     - ``field >= number``
     - Field is greater than or equal to the number
     -
   * - ``<=``
     - ``field <= number``
     - Field is less than or equal to the number
     -

Keyword forms and logical keywords must be uppercase. These searches are
equivalent:

.. code-block:: text

   artist : radiohead
   artist HAS radiohead

Use numeric fields with ``>``, ``<``, ``>=``, or ``<=``. For example:

.. code-block:: text

   playcount > 10
   rating >= 4
   bitrate >= 1000

Present and Missing Fields
--------------------------

Use ``PRESENT`` and ``MISSING`` to test whether a field has a value:

.. code-block:: text

   lyrics PRESENT
   composer MISSING

They can also be negated:

.. code-block:: text

   lyrics NOT PRESENT
   composer NOT MISSING

Combining Conditions
--------------------

Use the uppercase keywords ``AND``, ``OR``, and ``XOR`` to combine conditions:

.. code-block:: text

   genre = jazz AND rating >= 4
   artist : miles davis OR artist : john coltrane
   lyrics PRESENT XOR comment PRESENT

``XOR`` matches when exactly one of its two conditions is true. Use ``NOT`` or
``!`` to negate a condition:

.. code-block:: text

   NOT genre = classical
   !lyrics PRESENT
   genre NOT = pop

Use parentheses to make grouping explicit when mixing logical operators:

``(playcount > 0 AND genre = rock) OR title : rock``

This finds played tracks whose genre is exactly "rock", together with any track
whose title contains "rock". A complete group can also be negated:

``!(playcount > 1 AND genre = classical)``

Date Searches
-------------

Use date operators with fields such as ``date``, ``addedtime``,
``firstplayed``, ``lastplayed``, ``createdtime``, and ``lastmodified``.

.. list-table::
   :widths: 20 35 45
   :header-rows: 1

   * - Keyword
     - Example
     - Meaning
   * - ``BEFORE``
     - ``date BEFORE 2000``
     - Earlier than the given date
   * - ``AFTER``
     - ``addedtime AFTER 2025-01-01``
     - Later than the given date
   * - ``SINCE``
     - ``firstplayed SINCE 2025-01-01``
     - On or after the given date
   * - ``DURING``
     - ``lastplayed DURING 2025-08``
     - Within the given period

``DURING`` uses the precision of the supplied value. It can select a year,
month, day, hour, minute, or second:

.. code-block:: text

   addedtime DURING 2025
   addedtime DURING 2025-08
   addedtime DURING 2025-08-30
   addedtime DURING "2025-08-30 14:30"

For a rolling period ending at the current time, use ``DURING LAST`` with an
optional positive count. Supported units are seconds, minutes, hours, days,
weeks, months, and years:

.. code-block:: text

   lastplayed DURING LAST WEEK
   addedtime DURING LAST 14 DAYS
   firstplayed DURING LAST 3 MONTHS

Sorting and Limiting Results
----------------------------

Append a sort expression to order search results. ``SORT BY`` sorts in
ascending order; use ``SORT DESCENDING BY`` for descending order:

.. code-block:: text

   ALL SORT BY %artist%
   playcount > 0 SORT DESCENDING BY %playcount%

The compact forms ``SORT+`` and ``SORT-`` select ascending and descending order
respectively:

.. code-block:: text

   SORT+ artist
   SORT- playcount

The sort value can be a field name or another supported FooScript expression.
Use ``LIMIT`` to keep no more than a given number of results:

``playcount > 0 SORT- playcount LIMIT 25``

``ALL`` matches every track and is useful when a query only needs to sort or
limit the library.

Autoplaylists
-------------

Autoplaylists provide separate **Query** and **Sort** fields.
See :doc:`../playlists/autoplaylists` for how filtering, ordering, and limits interact.
