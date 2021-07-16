  
from ._version import __version__
from .utils.utils import check_package
from .io.pathways import read_dataset
from .io.pathways_frame import PathwaysFrame
from .io.static_layer import StaticLayerItem

# Check installed packages versions
check_package('pandas', '>=0.25.0')
check_package('geopandas', '>=0.6.0')
check_package('requests', '>=2.0.0')


__all__ = [
    '__version__',
    'PathwaysFrame',
    'StaticLayerItem',
    'read_dataset'
]