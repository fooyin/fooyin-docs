Scripting - Functions
=====================

FooScript functions manipulate strings, perform calculations, look up metadata,
and control script evaluation.

Numeric
-------

.. list-table::
   :class: scripting-functions
   :widths: 35 65
   :header-rows: 1

   * - **Function**
     - **Description**
   * - ``$add(x,y,…)``
     - Adds numeric arguments
   * - ``$sub(x,y,…)``
     - Subtracts later values from the first
   * - ``$mul(x,y,…)``
     - Multiplies numeric arguments
   * - ``$div(x,y)``
     - Divides the first value by the second
   * - ``$min(x,y,…)``
     - Returns the smallest numeric value
   * - ``$max(x,y,…)``
     - Returns the largest numeric value
   * - ``$mod(x,y)``
     - Returns the remainder of a division
   * - ``$rand(min,max)``
     - Returns a random number in the specified range
   * - ``$round(value[,precision])``
     - Rounds a numeric value, optionally to the specified precision
   * - ``$num(value,length)``
     - Formats a number with leading zeroes
   * - ``$timems(milliseconds)``
     - Formats milliseconds as ``wk d HH:mm:ss``

String
------

.. list-table::
   :class: scripting-functions
   :widths: 35 65
   :header-rows: 1

   * - **Function**
     - **Description**
   * - ``$replace(text,from,to,…)``
     - Replaces text fragments
   * - ``$ascii(text)``
     - Converts text to ASCII
   * - ``$slice(text,start[,end])``
     - Returns a slice of text
   * - ``$chop(text,count)``
     - Removes characters from the end
   * - ``$left(text,count)``
     - Returns characters from the left
   * - ``$right(text,count)``
     - Returns characters from the right
   * - ``$insert(text,insert[,pos])``
     - Inserts text at a position
   * - ``$substr(text,start,end)``
     - Returns a substring
   * - ``$strstr(text,needle[,start])``
     - Finds a substring position
   * - ``$stristr(text,needle[,start])``
     - Finds a substring position, ignoring case
   * - ``$strstrlast(text,needle[,start])``
     - Finds the last substring position
   * - ``$stristrlast(text,needle[,start])``
     - Finds the last substring position, ignoring case
   * - ``$split(text,sep,index)``
     - Returns one split segment using a 1-based index
   * - ``$join(sep,value,…)``
     - Joins non-empty values with a separator
   * - ``$len(text)``
     - Returns the text length
   * - ``$longest(a,b,…)``
     - Returns the longest string
   * - ``$strcmp(a,b)``
     - Compares two strings for equality
   * - ``$stricmp(a,b)``
     - Compares two strings for equality, ignoring case
   * - ``$longer(a,b)``
     - Tests whether ``a`` is longer than ``b``
   * - ``$sep()``
     - Returns the unit separator character
   * - ``$crlf([count])``
     - Returns one newline, or ``count`` newlines
   * - ``$tab([count])``
     - Returns one tab character, or ``count`` tab characters
   * - ``$swapprefix(text[,prefix,…])``
     - Moves leading articles to the end. The default prefixes are ``A`` and ``The``
   * - ``$stripprefix(text[,prefix,…])``
     - Removes leading articles. The default prefixes are ``A`` and ``The``
   * - ``$pad(text,length[,char])``
     - Pads text on the right
   * - ``$padright(text,length[,char])``
     - Pads text on the left
   * - ``$repeat(text,count)``
     - Repeats text
   * - ``$trim(text)``
     - Trims surrounding whitespace
   * - ``$lower(text)``
     - Converts text to lowercase
   * - ``$upper(text)``
     - Converts text to uppercase
   * - ``$abbr(text[,length])``
     - Builds an abbreviation, unless ``text`` is no longer than ``length``
   * - ``$caps(text)``
     - Capitalises words
   * - ``$elide_end(text,width[,delim])``
     - Elides text at the end
   * - ``$elide_mid(text,width[,delim])``
     - Elides text in the middle
   * - ``$urlencode(text)``
     - Percent-encodes text for use in URLs
   * - ``$isalpha(text)``
     - Checks whether text contains only alphabetic characters
   * - ``$isalnum(text)``
     - Checks whether text contains only alphanumeric characters
   * - ``$isnum(text)``
     - Checks whether text contains only numeric characters

Path
----

.. list-table::
   :class: scripting-functions
   :widths: 35 65
   :header-rows: 1

   * - **Function**
     - **Description**
   * - ``$directory(path,level)``
     - Returns a directory name from a path
   * - ``$directory_path(path)``
     - Returns the absolute directory path
   * - ``$ext(path)``
     - Returns a file extension
   * - ``$filename(path)``
     - Returns a filename without its extension

Utility
-------

.. list-table::
   :class: scripting-functions
   :widths: 35 65
   :header-rows: 1

   * - **Function**
     - **Description**
   * - ``$progress(pos,total,length,marker,background)``
     - Builds a text progress bar
   * - ``$progress2(pos,total,length,filled,background)``
     - Builds an alternate text progress bar
   * - ``$doclink(label,url)``
     - Builds a clickable document or web link
   * - ``$cmdlink(label,id)``
     - Builds a clickable link to a fooyin command

Time
----

.. list-table::
   :class: scripting-functions
   :widths: 35 65
   :header-rows: 1

   * - **Function**
     - **Description**
   * - ``$year(time)``
     - Returns the four-digit year from a date
   * - ``$month(time)``
     - Returns the two-digit month from a date
   * - ``$day_of_month(time)``
     - Returns the two-digit day of the month from a date
   * - ``$date(time)``
     - Returns the date formatted as ``YYYY-MM-DD``
   * - ``$time(time)``
     - Returns the time formatted as ``HH:MM`` or ``HH:MM:SS``

Script variables
----------------

These functions store and retrieve values during evaluation of a script.

.. list-table::
   :class: scripting-functions
   :widths: 35 65
   :header-rows: 1

   * - **Function**
     - **Description**
   * - ``$get(name)``
     - Returns the value stored in a script variable
   * - ``$put(name,value)``
     - Stores a script variable and returns the value
   * - ``$puts(name,value)``
     - Stores a script variable and returns nothing

Conditional
-----------

.. list-table::
   :class: scripting-functions
   :widths: 35 65
   :header-rows: 1

   * - **Function**
     - **Description**
   * - ``$and(expr,…)``
     - Returns true when all expressions are true
   * - ``$not(expr)``
     - Returns the opposite truth value
   * - ``$or(expr,…)``
     - Returns true when at least one expression is true
   * - ``$xor(expr,…)``
     - Returns true when an odd number of expressions are true
   * - ``$if(condition,then[,else])``
     - Returns ``then`` when ``condition`` is true; otherwise returns ``else``, if provided
   * - ``$if2(value[,fallback])``
     - Returns ``value`` if non-empty; otherwise returns ``fallback``, if provided
   * - ``$if3(a1,a2,…,aN,else)``
     - Returns the first true value from the list, or ``else`` when none match
   * - ``$ifgreater(x,y,then,else)``
     - Returns ``then`` when ``x`` is greater than ``y``; otherwise returns ``else``
   * - ``$iflonger(text,length,then,else)``
     - Returns ``then`` when ``text`` is longer than ``length``; otherwise returns ``else``
   * - ``$ifequal(x,y,then,else)``
     - Returns ``then`` when ``x`` and ``y`` are equal; otherwise returns ``else``

Lookup
------

.. list-table::
   :class: scripting-functions
   :widths: 35 65
   :header-rows: 1

   * - **Function**
     - **Description**
   * - ``$meta(field)``
     - Looks up a raw tag field by name. Multiple values are joined with ``", "``
   * - ``$meta(field,index)``
     - Looks up a raw tag field by name and returns the zero-based indexed value
   * - ``$meta_sep(field,sep)``
     - Looks up a raw tag field by name. Multiple values are joined with ``sep``
   * - ``$meta_sep(field,sep,lastsep)``
     - Looks up a raw tag field by name, using ``lastsep`` between the final two values
   * - ``$meta_test(field,…)``
     - Returns 1 when all named tag fields exist
   * - ``$meta_num(field)``
     - Returns the number of values in a raw tag field
   * - ``$info(field)``
     - Looks up technical track information
