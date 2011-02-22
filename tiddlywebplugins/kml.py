"""
A serializer for kml files
"""
from tiddlyweb.serializations import SerializationInterface

class Serialization(SerializationInterface):
    pass

def init(config):
    """
    add the serialization for content type application/vnd.google-earth.kml+xml
    """
    mime_type = 'application/vnd.google-earth.kml+xml'
    config['extension_types']['kml'] = mime_type
    config['serializers'][mime_type] = ['tiddlywebplugins.kml',
        '%s; charset=UTF8' % mime_type]
