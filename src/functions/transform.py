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


def transform_wgs84_to_cs92(lon: float, lat: float) -> tuple:
    """
    Transformer that will convert (EPSG:4326 (WGS 84)) to (EPSG:2180 (CS92))
    :param lon: longitude parameter of geo coordinates (EPSG:4326 (WGS 84))
    :param lat: latitude parameter of geo coordinates (EPSG:4326 (WGS 84))
    :return: x and y (EPSG:2180 (CS92))
    """
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:2180", always_xy=True)
    x, y = transformer.transform(lon, lat)
    return x, y
