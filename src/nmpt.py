import re

from src.api.functions import get_all_layers, get_request
from src.api.utils.nmt import Nmt

c = re.compile("\{{1}.*\}{1}")


def get_nmpt(x, y):
    """
    Gets a list of available NMPT data for a point with coordinates in the PUWG1992 system
    """

    URL = "https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMPT/WMS/SkorowidzeUkladEVRF2007?"
    layers = get_all_layers(url=URL, service='WMS')

    PARAMS = {
        'SERVICE': 'WMS',
        'request': 'GetFeatureInfo',
        'version': '1.3.0',
        'layers': ','.join(layers),
        'styles': '',
        'crs': 'EPSG:2180',
        'bbox': '%f,%f,%f,%f' % (y-50, x-50, y+50, x+50),
        'width': '101',
        'height': '101',
        'format': 'image/png',
        'transparent': 'true',
        'query_layers': ','.join(layers),
        'i': '50',
        'j': '50',
        'INFO_FORMAT': 'text/html'
    }
    resp = get_request(params=PARAMS, url=URL)

    if resp[0]:
        nmtElements = c.findall(resp[1])
        nmtList = []
        for nmtElement in nmtElements:
            element = nmtElement.strip("{").strip("}").split(',')
            params = {}
            for el in element:
                item = el.strip().split(':')
                val = item[1].strip('"')
                if len(item) > 2:
                    val = ":".join(item[1:]).strip('"')
                params[item[0]] = val
            nmt = Nmt(**params)
            nmtList.append(nmt)
        return True, nmtList
    else:
        return resp
