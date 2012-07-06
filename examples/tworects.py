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
Create 4 rectangles

- source
- target
- two obstacles

Two lines are routed from source to target avoiding obstacles.
"""

import arouter

router = arouter.Router()

s = router.add(((0, 100), (20, 120)))
o1 = router.add(((100, 50), (120, 70)))
o2 = router.add(((100, 80), (120, 140)))
o3 = router.add(((150, 130), (170, 160)))
d = router.add(((200, 100), (220, 120)))


l1 = router.connect(s, d)
l2 = router.connect(s, d)
l3 = router.connect(s, d)
l4 = router.connect(s, d)
l5 = router.connect(s, d)

router.route()

print(router.edges(l1))
print(router.edges(l2))

# vim: sw=4:et:ai
