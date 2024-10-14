Searching
=======================

Advanced searching can be carried out using a case-insensitive query-based language. It builds on the normal scripting syntax, offering more advanced filtering capabilities with operators, keywords, and logical grouping.

Operators
----------

Operators are used to compare metadata fields against values. Each operator has a specific meaning, and some have equivalent keywords for convenience.

.. list-table::
   :widths: 10 20 30 20  
   :header-rows: 1

   * - Operator
     - Syntax
     - Description
     - Keyword Equivalent
   * - `:`  
     - `field : string`  
     - Field contains the given string  
     - `HAS`  
   * - `=`  
     - `field = string`  
     - Field is exactly equal to the given string  
     - `IS`  
   * - `!=`  
     - `field != string`  
     - Field is not equal to the given string  
     -  
   * - `>`  
     - `field > number`  
     - Field is greater than the given number  
     - `GREATER`  
   * - `<`  
     - `field < number`  
     - Field is less than the given number  
     - `LESS`  
   * - `>=`  
     - `field >= number`  
     - Field is greater than or equal to the given number  
     -  
   * - `<=`  
     - `field <= number`  
     - Field is less than or equal to the given number  
     -  
   * - `!`  
     - `!expression`  
     - Expression is negated (not true)  
     - `NOT`  

Keywords
---------

Keywords allow more complex filtering by defining conditions, grouping expressions, and sorting results.

.. list-table::  
   :widths: 10 40 50  
   :header-rows: 1

   * - Keyword  
     - Syntax  
     - Description  
   * - `PRESENT`  
     - `field PRESENT`  
     - Returns tracks with the given metadata field  
   * - `MISSING`  
     - `field MISSING`  
     - Returns tracks missing the given metadata field  
   * - `BEFORE`  
     - `time1 BEFORE time2`  
     - Tracks where `time1` is before `time2`  
   * - `AFTER`  
     - `time1 AFTER time2`  
     - Tracks where `time1` is after `time2`  
   * - `SINCE`  
     - `time1 SINCE time2`  
     - Tracks where `time1` is at or after `time2`  
   * - `DURING`  
     - `time1 DURING time2`  
     - Tracks where `time1` falls within `time2`  
   * - `AND`  
     - `expression1 AND expression2`  
     - Tracks where both expressions are true  
   * - `OR`  
     - `expression1 OR expression2`  
     - Tracks where at least one expression is true  
   * - `XOR`  
     - `expression1 XOR expression2`  
     - Tracks where exactly one expression is true  
   * - `ALL`  
     - `ALL`  
     - Returns all tracks  
   * - `SORT BY`  
     - `SORT BY expression`  
     - Sort tracks in ascending order by the given expression  
   * - `SORT ASCENDING BY`  
     - `SORT ASCENDING BY expression`  
     - Equivalent to `SORT BY`  
   * - `SORT DESCENDING BY`  
     - `SORT DESCENDING BY expression`  
     - Sort tracks in descending order by the given expression  

Grouping Expressions
---------------------

Expressions can be grouped using parentheses `()` to control the order of operations. For example:

`(playcount > 0 AND genre = rock) OR title : rock`

This query returns tracks where either:

- The play count is greater than 0 **and** the genre is "rock",  
- **Or** the title contains the word "rock".  

Negation of groups is also possible using the `!` (not) operator:

`!(playcount > 1 AND genre = classical)`

This query returns all tracks **except** those where:

- The play count is greater than 1 **and** the genre is "classical".

Examples
--------------

1. Find all tracks with a play count greater than 10: 
   
    `playcount > 10`

2. Tracks where the genre is "jazz" but not "pop": 
   
    `genre = jazz AND genre != pop`

3. Tracks released since 2020, sorted by play count in descending order:

    `date SINCE 2020 SORT DESCENDING BY %playcount%`