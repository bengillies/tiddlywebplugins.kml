"""
A serializer for kml files
"""
from tiddlyweb.serializations import SerializationInterface

from pykml.factory import KML_ElementMaker as KML
from pykml.factory import ATOM_ElementMaker as ATOM
from lxml import etree

class Serialization(SerializationInterface):
    """
    This is the meat of the plugin. It provides 3 functions that enable it to
    serialize and deserialize tiddlers, and serialize lists of tiddlers (aka
    bags).
    """
    def tiddler_as(self, tiddler):
        """
        serialize a tiddler into kml format
        """
        kml = self.tiddler_to_kml(tiddler)
        return self.kml_to_string(kml)

    def list_tiddlers(self, tiddlers):
        """
        serialize a list of tiddlers into kml format
        """
        kml = KML.kml(KML.Document())
        for tiddler in tiddlers:
            tiddler_kml = self.tiddler_to_kml(tiddler)
            kml_inner = getattr(tiddler_kml, 'Placemark', None)
            if kml_inner is not None:
                kml.Document.append(kml_inner)

        return self.kml_to_string(kml)

    def tiddler_to_kml(self, tiddler):
        """
        convert one tiddler into a kml representation as an etree
        """
        geo_long = tiddler.fields.get('geo.long')
        geo_lat = tiddler.fields.get('geo.lat')
        if geo_long is not None and geo_lat is not None:
            kml = KML.kml(
                KML.Placemark(
                    KML.name(tiddler.title),
                    KML.description(tiddler.fields.get('description', '')),
                    KML.Point(
                        KML.coordinates('%s,%s' % (geo_long, geo_lat))
                    )
                )
            )
        else:
            kml = KML.kml()

        return kml

    def kml_to_string(self, kml):
        """
        convert an etree representation of kml to a valid xml document in
        string format
        """
        return '<?xml version="1.0" encoding="UTF-8"?>%s' % etree.tostring(kml)


def init(config):
    """
    add the serialization for content type application/vnd.google-earth.kml+xml
    """
    mime_type = 'application/vnd.google-earth.kml+xml'
    config['extension_types']['kml'] = mime_type
    config['serializers'][mime_type] = ['tiddlywebplugins.kml',
        '%s; charset=UTF8' % mime_type]
