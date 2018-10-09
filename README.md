# THE HOURS

The Hours is an ongoing 'rice' project, aimed at making a theme for my LXDE / Openbox installation for home / personal use.

The Hours aims to create multiple color schemes, depending on the time of day at which the PC was switched on, and apply these color schemes to Openbox windows, LXTerminal and conky or other bar applications based on the colors in any wallpaper(s) that are used.

Specified below is a layout for the actions the script(s) should take to generate the color schemes, and output the config files needed for the applications to use these colors. This layout will also serve as a 'to do list' and basic skeleton for the scripts that need to be written while the project is in process.

## The List  

1.    The Hours will create all the folders and files needed for the scripts to work. This should be:
      * A wallpaper folder for each color scheme
      * A .themes folder containing the config files
      * A rc.xml for Openbox in the .config folder
      * A lxterminal.conf setting for each color scheme
      * Adding an autorun script to set the correct scheme at startup

2.    The Hours should read (pre-defined?) folders containing wallpaper images for each Time of Day schemes.
  2.   The Hours will screen all the image files in these folders, and generate a list of the most common colors used in the images.
  2.   The Hours will write these colorcodes to a script that replaces the appropriate lines in lxterminal.conf and rc.xml for each scheme when requested, either at startup or by the user's command.

3.    Upon starting, The Hours should set a wallpaper and color scheme to match the current time of day.
  3.    These schemes are:    
        * dawn  - 06 to 12
        * day   - 12 to 18
        * dusk  - 18 to 00
        * dark  - 00 to 06

4.    The Hours should have a command line interface to change the color scheme at the user's command.
  4.    This command should be able to change either 'all' the parts of the color scheme, or 'select'
    4. Setting all parts of the color scheme at the same time should be done by terminal, to either the scheme corresponding to the current time, i.e. 'thehours -set all', or to a specific color scheme, i.e. 'thehours -set all day'
    4. Select parts to be set:
        * the Background image (folder) : 'thehours -set bg dusk'
        * The Window colors (Openbox) : 'thehours -set wm dawn'
        * The Terminal colors (LXTerminal) : 'thehours -set term dark'
        * The clock, bars and panels (conky/tint2) : 'thehours -set bars day'
  4. When a whole new scheme is required (for example, when all the wallpaper images have been changed), thehours should have a reset function to re-create a new list of most common colors used in the wallpapers, i.e. 'thehours -reset'. This will run through all the steps in 2. and will result in setting the new color scheme for all parts of the theme.

## Installation and usage

To be added at a later date, when actual code has been written!
