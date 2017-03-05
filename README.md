File Content extension for Python-Markdown
==================================

This extension adds file content formating to [Python-Markdown].

[Python-Markdown]: https://github.com/waylan/Python-Markdown

Installation
------------

### Install locally

```
git clone https://github.com/PingTrip/python-markdown-file_content.git
cd python-markdown-file_content
setup.py build
setup.py install
```

Usage
-----
The extension name is `file_content` so you need to add that name to your list of Python-Markdown extensions.
Check [Python-Markdown documentation](http://pythonhosted.org/Markdown/extensions/) for details on how to load extensions.

Example:
```
~@C:\filename.txt
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare.
~@
```

![Alt text](/../screenshots/example.png?raw=true "Example File Content")
