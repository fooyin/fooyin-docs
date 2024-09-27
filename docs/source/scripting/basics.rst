Scripting - Basics
===================

FooScript is a scripting language integrated into fooyin, offering advanced user configuration for many widgets. 
This section will introduce you to the basics of FooScript, including function calls, variable usage, and basic formatting.

Fields
------

At its core, FooScript allows you to retrieve information from the tag fields of your music files using variables enclosed in percent signs (``%``). For example:

``%album%``

The script above retrieves the album tag of the track. If the album tag is missing, it will return an empty result. You can use this syntax to access any tag field. For instance, if you have a custom tag named `subalbum`, you would use ``%subalbum%`` to access its information.

Additionally, the same syntax is used for accessing technical information, e.g., ``%bitrate%`` returns the file's bitrate or ``%samplerate%`` returns the sample rate.

Field Remappings
----------------

In FooScript, some variables are remapped to simplify retrieving certain fields. For example, ``%albumartist%`` will return the album artist tag of a track if it exists. If it does not, it will return the first non-empty field from the following list: ``artist``, ``composer``, ``performer``.

If you need to access the raw value of a field without any remapping, you can use the `meta` function. For example:

``$meta(artist)``

This will retrieve the exact value of the artist field without any fallback to other fields.

Functions
---------

FooScript also includes a variety of functions, which are used to compute expressions and manipulate data. Functions take one or more arguments, process them, and return a result. Here's an example:

``$repeat(a,10)``

The function above repeats the letter "a" ten times.

Every function in FooScript begins with a dollar sign (``$``) followed by the function's name. The arguments are placed in parentheses immediately after the function name. If a function requires multiple arguments, they should be separated by commas, with no spaces in the entire expression.

Some functions do not require any arguments. For example:

``$crlf()``

This function adds a carriage return and line feed, which is useful for displaying the result over several lines.

Control Functions
-----------------

Control functions in FooScript allow you to evaluate conditions and perform different actions based on the result.

One of the most useful control functions is the `if` statement, which follows this syntax in FooScript:

``$if(%artist%,%artist%,%albumartist%)``

In this example, fooyin checks whether the ``artist`` tag is present for the track. If it is found, the second argument (``artist``) is evaluated, and the artist's name is returned. If the ``artist`` tag is not present, the third argument (``albumartist``) is evaluated, and the album artist is returned instead.

The above script can be simplified using the `if2` function:

``$if2(%artist%,%albumartist%)``

The `if2` function checks if the first argument (``artist``) is present and returns it. If the first argument is missing or empty, it returns the second argument (``albumartist``).

Conditionals
------------

Conditionals are another way to control results. The syntax for a conditional is to place the condition within square brackets ``[ ]``. If the condition inside the brackets evaluates to true, the result is returned; otherwise, it returns nothing. For instance:

``[%album% - ]%title%``

In this example, if the ``album`` tag exists and is not empty, the following is returned:

``album - title``

If the ``album`` tag is missing or empty, then it will just return:

``title``