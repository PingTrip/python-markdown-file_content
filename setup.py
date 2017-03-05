#!/usr/bin/env python

from distutils.core import setup

long_description = \
"""This extension adds math formulas support to Python-Markdown_
(works with version 2.6 or newer).

.. _Python-Markdown: https://github.com/waylan/Python-Markdown

You can find the source on GitHub_.
Please refer to the `README file`_ for details on how to use it.

.. _GitHub: https://github.com/PingTrip/python-markdown-file_content
.. _`README file`: https://github.com/PingTrip/python-markdown-file_content/blob/master/README.md
"""

setup(name='python-markdown-file_content',
      description='File Content extension for Python-Markdown',
      long_description=long_description,
      author='Dave Crawford',
      author_email='pingtrip@gmail.com',
      version='0.9',
      url='https://github.com/PingTrip/python-markdown-file_content',
      py_modules=['file_content'],
      license='BSD')
