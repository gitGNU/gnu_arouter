/*
 * ARouter - line routing using libavoid library.
 *
 * Copyright (C) 2010 by Artur Wroblewski <wrobell@pld-linux.org>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <libavoid/libavoid.h>

#ifdef  __cplusplus
extern "C" {
#endif

Avoid::Router *create_router();
Avoid::ShapeRef *add_shape(Avoid::Router *router, double p[2][2]);
Avoid::ConnRef *connect_shapes(Avoid::Router *router, Avoid::ShapeRef *start, Avoid::ShapeRef *end);
Avoid::ConnRef *connect_points(Avoid::Router *router, double start[2], double end[2]);
void route(Avoid::Router *router);
double **get_points(Avoid::ConnRef *connector, unsigned int *n);

#ifdef  __cplusplus
}
#endif

