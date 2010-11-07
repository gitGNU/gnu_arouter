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

import arouter

router = arouter.Router()

r1 = router.add(((0, 100), (20, 120)))
r2 = router.add(((100, 80), (120, 140)))
r3 = router.add(((150, 130), (170, 160)))
r4 = router.add(((200, 100), (220, 120)))


l = router.connect(r1, r4)

router.route()

print router.edges(l)

# vim: sw=4:et:ai
