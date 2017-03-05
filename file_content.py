# -*- coding: utf-8 -*-
'''
File Content Extension for Python Markdown
=========================================
This extension adds file content blocks to Python-Markdown.

See <https://pingtrip.com/weblog/file_content.html> for documentation.

Author: 2015-2017, Dave Crawford http://pingtrip.com/
'''

from __future__ import absolute_import
from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re


class FileContentExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)

        md.preprocessors.add('file_content',
                             FileContentPreprocessor(md),
                             ">normalize_whitespace")


class FileContentPreprocessor(Preprocessor):
    FILE_CONTENT_RE = re.compile(r'''~@(.+?)\n  # $1 = Filename
                                     (.+?)      # $2 = File Contents
                                     ~@         # closing syntax''', re.MULTILINE | re.DOTALL | re.VERBOSE)

    FILE_WRAP = '<table class=\"FileListing\">\n\t<tr class=\"fname\">\n\t\t<td><b>File:</b> %s</td>\n\t</tr>\n\t<tr class=\"fcontent\">\n\t\t<td><pre class=\"fcontentScroller\">\n%s</pre></td>\n\t</tr>\n</table>\n\n'

    def __init__(self, md):
        super(FileContentPreprocessor, self).__init__(md)

    def run(self, lines):
        """ Match and store File Content Blocks in the HtmlStash. """

        text = "\n".join(lines)

        while 1:
            m = self.FILE_CONTENT_RE.search(text)

            if m:
                content = self.FILE_WRAP % (m.group(1), self._escape(m.group(2)))
                placeholder = self.markdown.htmlStash.store(content, safe=True)
                text = "{}\n{}\n{}".format(text[:m.start()], placeholder, text[m.end():])
            else:
                break

        return text.split("\n")

    def _escape(self, txt):
        """ basic html escaping """
        txt = txt.replace('&', '&amp;')
        txt = txt.replace('<', '&lt;')
        txt = txt.replace('>', '&gt;')
        txt = txt.replace('"', '&quot;')
        return txt


def makeExtension(*args, **kwargs):
    return FileContentExtension(*args, **kwargs)
