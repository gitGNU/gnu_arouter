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
Create 7 rectangles

- source
- target
- 3 obstacles
- container having source and one of the obstacles

Two lines are created (avoiding obstacles)
- from source to target (container is ignored)
- from container to target
"""

import arouter

router = arouter.Router()

s = router.add(((0, 100), (20, 120)))
o1 = router.add(((100, 80), (120, 140)))
o2 = router.add(((150, 130), (170, 160)))
t = router.add(((200, 100), (220, 120)))

# add container and one more obstacle (just below source)
c = router.add(((-5, 95), (25, 150)))
o3 = router.add(((0, 125), (20, 145)))

l1 = router.connect(s, t)
l2 = router.connect(c, t)

router.route()

print(router.edges(l1))
print(router.edges(l2))

# vim: sw=4:et:ai
