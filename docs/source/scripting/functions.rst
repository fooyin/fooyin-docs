Scripting - Functions
=====================

FooScript offers a variety of functions that allow you to manipulate strings, perform calculations, and control logic. These functions can be used anywhere:

Arithmetic
----------

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Function**
     - **Description**
   * - $add(x,y)
     - Adds `x` and `y`
   * - $sub(x,y)
     - Subtracts `y` from `x`
   * - $mul(x,y)
     - Multiplies `x` and `y`
   * - $div(x,y)
     - Divides `x` by `y`
   * - $min(x,y)
     - Returns the minimum of `x` and `y`
   * - $max(x,y)
     - Returns the maximum of `x` and `y`
   * - $mod(x,y)
     - Remainder from dividing `x` by `y`

Control
-------

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Function**
     - **Description**
   * - $longer(str1,str2)
     - Returns `true` if `str1` is longer than `str2`, otherwise `false`
   * - $if(cond,then)
     - Evaluates the condition `cond`; returns `then` if true, otherwise `false`
   * - $if(cond,then,else)
     - Evaluates the condition `cond`; returns `then` if true, otherwise `else`
   * - $if2(expr,else)
     - Evaluates the expression `expr`; returns `expr` if true, otherwise returns `else`
   * - $ifgreater(x,y,then,else)
     - Returns `then` if `x` is greater than `y`, otherwise `else`
   * - $iflonger(str1,str2,then,else)
     - Returns `then` if `str1` is longer than `str2`, otherwise `else`
   * - $ifequal(x,y,then,else)
     - Returns `then` if `x` is equal to `y`, otherwise `else`

String
------

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Function**
     - **Description**
   * - $num(nbr,len)
     - Formats the integer number `nbr` as a string. Pads with zeros from the left until size `len` is reached
   * - $replace(str,search,replace)
     - Replaces all occurrences of `search` in `str` with `replace`
   * - $slice(str,pos)
     - Returns substring of `str` starting at position `pos` and extending to its end
   * - $slice(str,pos,n)
     - Returns substring of `str` of length `n` starting at position `pos`
   * - $chop(str,n)
     - Removes the last `n` characters from `str`
   * - $left(str,len)
     - Returns the first `len` characters from the left of `str`
   * - $right(str,len)
     - Returns the first `len` characters from the right of `str`
   * - $insert(str,ins,n)
     - Inserts `ins` into `str` after `n` characters
   * - $substr(str,start,end)
     - Returns substring of `str`, starting from `start` and ending at `end`
   * - $len(str)
     - Length of `str`
   * - $longest(arg,…)
     - Returns the longest of all arguments
   * - $strcmp(str1,str2)
     - Compares `str1` and `str2` for equality, case-sensitive.
   * - $stricmp(str1,str2)
     - Compares `str1` and `str2` for equality, case-insensitive
   * - $sep()
     - Returns the native directory separator
   * - $crlf()
     - Inserts end-of-line marker (carriage return, line feed). Can be used to output multiple lines
   * - $tab()
     - Inserts one tab character.
   * - $tab(count)
     - Inserts `count` tab character.
   * - $swapprefix(str)
     - Moves `A` and `The` prefixes to the end of `str`
   * - $swapprefix(str,prefix1,…)
     - Moves all specified prefixes to the end of `str`
   * - $stripprefix(str)
     - Removes `A` and `The` prefixes from `str`
   * - $stripprefix(str,prefix1,…)
     - Removes all specified prefixes from `str`
   * - $pad(str,len)
     - Creates a left-aligned version of `str` by adding spaces to the right until length `len` is reached
   * - $pad(str,len,char)
     - Creates a left-aligned version of `str` by adding `char` to the right until length `len` is reached
   * - $padright(str,len)
     - Creates a right-aligned version of `str` by adding spaces to the left until length `len` is reached
   * - $padright(str,len,char)
     - Creates a right-aligned version of `str` by adding `char` to the left until length `len` is reached
   * - $repeat(str,count)
     - Returns `count` copies of `str`
   * - $trim(str)
     - Removes leading and trailing whitespace from `str`
   * - $lower(str)
     - Converts `str` to lowercase
   * - $upper(str)
     - Converts `str` to uppercase
   * - $abbr(str)
     - Returns abbreviation of `str`
   * - $abbr(str,len)
     - Returns abbreviation of `str` if longer than `len` characters, otherwise returns `str`
   * - $caps(str)
     - Capitalises the first letter of each word in `str`
   * - $directory(path)
     - Returns the directory name of a given filepath
   * - $directory_path(path)
     - Returns the directory path of a given file path
   * - $ext(path)
     - Returns the file extension of a given filename or filepath
   * - $filename(path)
     - Returns the filename from a given filepath
   * - $progress(pos,range,len,char1,char2)
     - Creates a progress bar in the format: `====#========`
   * - $progress2(pos,range,len,char1,char2)
     - Creates a progress bar in the format: `#####========`
   * - $timems(ms)
     - Formats the given time in milliseconds to: `wk d HH:mm:ss`