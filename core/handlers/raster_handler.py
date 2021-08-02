# -*- coding: utf-8 -*-

"""
/***************************************************************************
 AlosContourExtractor
                                 A QGIS plugin
 Creates contour and elevation points from Alos Palsar DEM
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-07-20
        copyright            : (C) 2021 by CamellOnCase
        email                : camelloncase@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Francisco Alves Camello Neto'
__date__ = '2021-07-20'
__copyright__ = '(C) 2021 by CamellOnCase'

from qgis.analysis import QgsGeometrySnapper, QgsInternalGeometrySnapper
from qgis.core import (edit, Qgis, QgsCoordinateReferenceSystem, QgsCoordinateTransform,
                       QgsExpression, QgsFeature, QgsFeatureRequest, QgsField, QgsGeometry, QgsMessageLog,
                       QgsProcessingContext, QgsProcessingMultiStepFeedback, QgsProcessingUtils, QgsProject,
                       QgsSpatialIndex, QgsVectorDataProvider, QgsVectorLayer, QgsVectorLayerUtils, QgsWkbTypes,
                       QgsProcessingFeatureSourceDefinition, QgsFeatureSink)
from qgis.PyQt.Qt import QObject, QVariant

class RasterHandler(QObject):
    """
    Docstring
    """

    def __init__(self, iface=None, parent=None):
        super(RasterHandler, self).__init__()
        self.parent = parent
        self.iface = iface
        if iface:
            self.canvas = iface.mapCanvas()
        # self.featureHandler = FeatureHandler(iface)
        # self.geometryHandler = GeometryHandler(iface)
        # self.algRunner = AlgRunner()

    def get_dem_extent(self, dem_raster):
        """
        Docstring
        :return: (QgsRectangle) raster bounding box
        """
        return dem_raster.extent()

