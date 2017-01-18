# The MIT License (MIT)
# Copyright (c) 2016 by the Cate Development Team and contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Description
===========

Select variables in a dataset.

Components
==========
"""

import geopandas as gpd
import json

from cate.core.op import op


@op(tags=['format', 'dataframe', 'geojson'])
def to_geojson(df: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Returns a GeoJSON string representation of the GeoDataFrame.

    :param df: The DataFrame.
    :return: A GeoJSON representation
    """

    return df.to_json()


@op(tags=['format', 'dataframe', 'json', 'properties'])
def to_json_props(df: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Returns a JSON string representation of all properties and features of the GeoDataFrame.

    :param df: The DataFrame.
    :return: A JSON representation
    """
    props = list()

    for feature in df.iterfeatures():
        del feature['geometry']
        props.append(feature)

    return json.dumps(props)
