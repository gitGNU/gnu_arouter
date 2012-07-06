#!/usr/bin/env python3

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


"""
Build setup for arouter library.
"""

from setuptools import setup, find_packages, Extension

avoid_module = Extension('_pyavoid',
   sources=['src/pyavoid.cxx'],
   libraries=['avoid'],
   include_dirs=['src'])

setup(
    name='arouter',
    version='0.2.0',
    author='Artur Wroblewski',
    author_email='wrobell@pld-linux.org',
    description="""Line router using libavoid library.""",
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries',
    ],
    package_dir={'': 'src'},
    packages=['arouter'],
    ext_modules=[avoid_module],
    include_package_data=True,
)

# vim: sw=4:et:ai
