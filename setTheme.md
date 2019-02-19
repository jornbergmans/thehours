What the setTheme script needs to do:

- Checks for the current Hour
- Sets variable theHour to one of the four possible settings
- Run getTheme for the correct colors to use
- Run the feh command generated for the theme to set wallpaper
- Pull the required config from its subfolder to the theme folder / live config for:
	* conky
	* gtkrc
	* openbox
	* terminal?
