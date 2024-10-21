Wiregock Validator Plugin
======================

This is a simple plugin for [Sublime Text](http://www.sublimetext.com) to allow for easily validation [Wiremock JSON config](https://wiremock.org/docs/request-matching/)

It takes the current opened file, and returns the URL to the clipboard.

Support
-------
Sublime Pastebin Plugin supports both [Sublime Text 2](http://www.sublimetext.com/2) and [Sublime Text 3](http://www.sublimetext.com/3) and [Sublime Text 4](http://www.sublimetext.com/)

Installation
------------

Clone this repo into your Sublime Text Packages directory
(replace 2 with 3 if you use sublime text 3 or with 4 if you use sublime text 4)
###Linux
    cd ~/.config/sublime-text-2/Packages/
    git clone git://github.com/rikkimongoose/WiregockValidator.git

###Mac
    cd ~/"Library/Application Support/Sublime Text 2/Packages/"
    git clone git://github.com/rikkimongoose/WiregockValidator.git
###Windows
    cd `%programfiles%/Sublime Text/Packages/`
    git clone git://github.com/rikkimongoose/WiregockValidator.git

Usage
-----

Open JSON file you're going to check, open console with `alt + ~` and hit `ctrl + alt + v`. All errors will be displayed in console.

*Good luck!*