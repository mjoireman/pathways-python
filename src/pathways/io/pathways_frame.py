
from geopandas.geodataframe import GeoDataFrame
from enum import Enum
from .static_layer import StaticLayerItem

class PathwaysDatasetTypes(Enum):
    static = "static"
    managed = "managed"
    studies = "studies"
    recommendations = "recommendations"
   

class PathwaysDatasetInfo():
    dataset_type: PathwaysDatasetTypes = None
    dataset_info: StaticLayerItem = None
 

class PathwaysFrame(GeoDataFrame):
 
    def is_pathways_frame(self):
        return True
    
    def set_pathways_info(self, info: PathwaysDatasetInfo):
        self.pathways_info = info

    def get_pathways_info(self) -> PathwaysDatasetInfo:
        return self.pathways_info
