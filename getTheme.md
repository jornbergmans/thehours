What the getTheme script should do:

Using the 'get' generator:
- Read the current Hour from the setTheme output
- Read the chosen background from the feh selection
- Read out the most prominent colors from the background image
- Sort these colors by their Luminance
- Format these colors into a dictionary and output that dict

Using the 'set' generator:
- Write new config files for the requested Hour for
  * feh (background)
  * conky
  * gtk-2.0
  * openbox
  * gtk 3 to be added in a future version