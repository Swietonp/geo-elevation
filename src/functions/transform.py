from pyproj import Transformer


def transform_cs92_to_wgs84(x: float, y: float) -> tuple:
    """
    Transformer that will convert EPSG:2180 (CS92) to EPSG:4326 (WGS 84)
    :param x: x parameter of geo coordinates (EPSG:2180 (CS92))
    :param y: y parameter of geo coordinates (EPSG:2180 (CS92))
    :return: longitude and latitude (EPSG:4326 (WGS 84))
    """
    transformer = Transformer.from_crs("EPSG:2180", "EPSG:4326", always_xy=True)
    lon, lat = transformer.transform(x, y)
    return lon, lat
