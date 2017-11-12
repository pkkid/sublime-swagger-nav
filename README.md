# Swagger Nav #

Sublime Text 2/3 plugin for quick navigation in Swagger files. This plugin is
based on the YAML Nav plugin written by Denis Diachkov. If you are looking for
a more general YAML Nav plugin, you can go check out that project at:
https://github.com/ddiachkov/sublime-yaml-nav.

The following changes have been applied to make it a bit nicer to work with
Swagger API files:

* List all top-level and second-level items.
* Only list deeper items if they are an object property.
* Follow $ref symbols to easily find sub-items in references. 

![screenshot](screenshot.png)

## Installation ##

### Install with Package Control ###

See http://wbond.net/sublime_packages/package_control/installation for
instructions. Open the palette (Control+Shift+P or Command+Shift+P) in Sublime
Text and select Package Control: Install Package and then select "Swagger Nav"
from the list.

### Manual Installation ###

 * cd <YOUR PACKAGES DIRECTORY> (eg. ~/Library/Application\ Support/Sublime\ Text\ 3/Packages)
 * git clone https://github.com/pkkid/sublime-swagger-nav

### Key Bindings ###

 * Command+R in Swagger source will run "goto_yaml_symbol" command.
 * Command+Shift+W in Swagger source will run "copy_yaml_symbol_to_clipboard" command.

### Localization YAML's ###

Since version 1.2.0 Swagger Nav tries to detect YAML's with localization data
(ie. Rails locales) and automatically strips first tag when symbol is copied to
the clipboard (Super+Shift+W). For example "en.active_record.attributes.entity.name"
will be copied as "active_record.attributes.entity.name". This behavior can be
disabled by setting ```"trim_language_tag_on_copy_from_locales": false``` in
configuration file ("Swagger Nav.sublime-settings").

### Symbols ###

Swagger Nav automatically trims leading colons from symbols. This behavior can
be disabled by setting ```"trim_leading_colon": false``` in configuration file
("Swagger Nav.sublime-settings").

## Licence

All of Swagger Nav is licensed under the MIT licence.

  Copyright (c) 2017 Michael Shepanski

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
