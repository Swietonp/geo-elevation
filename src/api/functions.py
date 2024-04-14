import time
import requests
import lxml.etree as ET

from src.api.adapter import get_legacy_session


def get_request(params, url):
    try:
        r = get_legacy_session().get(url=url, params=params, verify=False)

    except requests.exceptions.ConnectionError:
        time.sleep(0.4)
        try:
            r = get_legacy_session().get(url=url, params=params, verify=False)

        except requests.exceptions.ConnectionError:
            return False, "Błąd połączenia"
    r_txt = r.text
    if r.status_code == 200:
        return True, r_txt
    else:
        return False, "Błąd %d" % r.status_code


def get_all_layers(url, service):
    params = {
        'SERVICE': service,
        'request': 'GetCapabilities',
        'INFO_FORMAT': 'text/html'
    }

    layers = get_request(params, url)
    parser = ET.XMLParser(recover=True)
    tree = ET.ElementTree(ET.fromstring(layers[1][56:].lstrip(), parser=parser))

    layers = [el.text for el in tree.iter() if 'Name' in str(el.tag) and str(el.text) != 'WMS']
    return layers
