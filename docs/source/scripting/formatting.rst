Scripting - Formatting
=======================

FooScript also supports formatting tags which can be used to apply various properties to the output text. 
Properties either extend to the end of the string, or until the matching closing tag. i.e. ``<b>Bold</b> Text``

These are currently only supported when used in the playlist:

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - **Function**
     - **Description**
   * - ``<b>``
     - **Bold**: Applies bold formatting to the text up
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