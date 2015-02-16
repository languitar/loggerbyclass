# ============================================================
#
# Copyright (C) 2014-2015 by Johannes Wienke <languitar at semipol dot de>
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

'''
Provides a single helper function to simplify the common idiom
of getting one logger object from python standard logging per
class.

@author: languitar
'''

import logging


def get_logger_by_class(klass, instance=None):
    """Gets a python logger instance based on a class instance. The logger name
    will be a dotted string containing python module and class name, hence
    being the full path to the class.

    @param klass: class instance
    @return: logger instance
    """
    return logging.getLogger(klass.__module__ + "." + klass.__name__ +
                             (".__{}__".format(instance.replace('.', '_'))
                              if instance else ""))
