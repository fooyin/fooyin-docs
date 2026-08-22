Formatting
==========

FooScript supports formatting tags that apply visual properties to output text.
Formatting can be used in most widgets that evaluate FooScript and display
text. Support may vary depending on the widget and the property being used.

Properties extend either to the end of the string or to the matching closing
tag. For example, ``<b>Bold</b> Text`` applies bold formatting only to the word
``Bold``.

.. list-table::
   :class: scripting-formatting
   :widths: 20 80
   :header-rows: 1

   * - **Tag**
     - **Description**
   * - ``<b>``
     - **Bold**: Applies bold formatting to the text
   * - ``<i>``
     - **Italic**: Applies italic formatting to the text
   * - ``<font=name>``
     - **Font Family**: Sets the font family for the text to ``name``
   * - ``<size=n>``
     - **Font Size**: Sets the font size for the text to ``n``
   * - ``<sized=n>``
     - **Font Size Delta**: Adjusts the font size by ``n`` relative to the current size
   * - ``<alpha=n>``
     - **Color Alpha**: Sets the transparency level of the text (0-255) to ``n``
   * - ``<rgb=r,g,b>``
     - **Color RGB**: Sets the color of the text (RGB)
   * - ``<rgb=r,g,b,a>``
     - **Color RGBA**: Sets the color of the text (RGBA)
