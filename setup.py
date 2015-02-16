# ============================================================
#
# Copyright (C) 2014 by Johannes Wienke <languitar at semipol dot de>
#
# This file may be licensed under the terms of the
# GNU Lesser General Public License Version 3 (the ``LGPL''),
# or (at your option) any later version.
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the LGPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the LGPL along with this
# program. If not, go to http://www.gnu.org/licenses/lgpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ============================================================

from setuptools import setup, find_packages

setup(name='loggerbyclass',
      version='0.2.0',
      description='''
                  Provides a single helper function to simplify the common idiom
                  of getting one logger object from python standard logging per
                  class.

                  The method get_logger_by_class returns a logger with the name
                  being the full path to that class separated by dots.
                  ''',
      author='Johannes Wienke',
      author_email='languitar@semipol.de',
      url='https://github.com/languitar/loggerbyclass.git',
      license='LGPLv3+',
      keywords=['logging', 'helper', 'utility'],
      classifiers=['Programming Language :: Python',
                   'Topic :: System :: Logging',
                   'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)'],
      py_modules=['loggerbyclass']
      )
