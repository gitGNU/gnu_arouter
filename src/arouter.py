#
# ARouter - line routing using libavoid library.
#
# Copyright (C) 2010 by Artur Wroblewski <wrobell@pld-linux.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sysconfig
import ctypes as ct
from ctypes.util import find_library

lib = ct.CDLL('_pyavoid{}'.format(sysconfig.get_config_var('SO')))
clib = ct.CDLL(find_library('c'))

Point = ct.c_double * 2
Rectangle = Point * 2


class Router(object):
    """
    Line router using libavoid library.
    """
    def __init__(self):
        self.router = lib.create_router()


    def add(self, shape):
        """
        Add a shape to router.
        """
        points = (Point(p[0], p[1]) for p in shape)
        rect = Rectangle(*points)
        ptr = lib.add_shape(self.router, rect)
        return ptr


    def connect(self, source, dest):
        """
        Connect two shapes with a line.
        """
        return lib.connect_shapes(self.router, source, dest)


    def edges(self, line):
        """
        Get edges of a line.
        """
        n = ct.c_uint()
        p_ptr = lib.get_points(line, ct.byref(n))
        p = ct.cast(p_ptr, ct.POINTER(ct.POINTER(ct.c_double) * n.value))
        edges = tuple((p.contents[i][0], p.contents[i][1]) for i in range(n.value))
        clib.free(p_ptr)
        return edges


    def route(self):
        """
        Perform routing operaton.
        """
        lib.route(self.router)


# vim: sw=4:et:ai
