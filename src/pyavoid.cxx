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


#include <pyavoid.h>
#include <stdio.h>

#define CONN_PIN    0x01

Avoid::Router *create_router() {
    //Avoid::Router *router = new Avoid::Router(Avoid::PolyLineRouting);
    Avoid::Router *router = new Avoid::Router(Avoid::OrthogonalRouting);

    router->setRoutingParameter(Avoid::segmentPenalty, 10);
    router->setRoutingParameter(Avoid::anglePenalty, 10);
    router->setRoutingParameter(Avoid::crossingPenalty, 4000);
    router->setRoutingParameter(Avoid::clusterCrossingPenalty, 0);

    router->setRoutingOption(Avoid::nudgeOrthogonalSegmentsConnectedToShapes, true);
    router->setOrthogonalNudgeDistance(13);
    return router;
}

Avoid::ShapeRef *add_shape(Avoid::Router *router, double p[2][2]) {
    Avoid::Rectangle rect(Avoid::Point(p[0][0], p[0][1]), Avoid::Point(p[1][0], p[1][1]));
    Avoid::ShapeRef *shape = new Avoid::ShapeRef(router, rect);
    new Avoid::ShapeConnectionPin(shape, CONN_PIN, Avoid::ATTACH_POS_CENTRE, Avoid::ATTACH_POS_CENTRE, 5);
    return shape;
}

Avoid::ConnRef *connect_shapes(Avoid::Router *router, Avoid::ShapeRef *start, Avoid::ShapeRef *end) {
    Avoid::ConnEnd s(start, CONN_PIN);
    Avoid::ConnEnd e(end, CONN_PIN);
    Avoid::ConnRef *connector = new Avoid::ConnRef(router, s, e);
    connector->setRoutingType(Avoid::ConnType_Orthogonal);
    return connector;
}

Avoid::ConnRef *connect_points(Avoid::Router *router, double start[2], double end[2]) {
    Avoid::Point p1(start[0], start[1]);
    Avoid::Point p2(end[0], end[1]);
    Avoid::ConnRef *connector = new Avoid::ConnRef(router, p1, p2);
    connector->setRoutingType(Avoid::ConnType_Orthogonal);
    return connector;
}

void route(Avoid::Router *router) {
    router->processTransaction();
    router->outputInstanceToSVG("pyavoid");
}

double **get_points(Avoid::ConnRef *connector, unsigned int *n) {
    Avoid::PolyLine line = connector->displayRoute();
    *n = line.size();
    double **points = new double*[*n];
    for (size_t i = 0; i < *n; ++i) {
        Avoid::Point point = line.at(i);
        points[i] = new double[2];
        points[i][0] = point.x;
        points[i][1] = point.y;
    }
    return points;
}

