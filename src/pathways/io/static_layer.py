from typing import List, Any, Optional, Union
from uuid import UUID

class SystemColumns:
    route_name_column: Optional[str]
    measure_column: Optional[str]
    from_measure_column: Optional[str]
    to_measure_column: Optional[str]

    def __init__(self, route_name_column: Optional[str], measure_column: Optional[str], from_measure_column: Optional[str], to_measure_column: Optional[str]) -> None:
        self.route_name_column = route_name_column
        self.measure_column = measure_column
        self.from_measure_column = from_measure_column
        self.to_measure_column = to_measure_column

    @classmethod
    def from_json(cls, data: dict):
        route_name_column = data["routeNameColumn"] if "routeNameColumn" in data else None
        measure_column = data["measureColumn"] if "measureColumn" in data else None
        from_measure_column= data["fromMeasureColumn"] if "fromMeasureColumn" in data else None
        to_measure_column= data["toMeasureColumn"] if "toMeasureColumn" in data else None
        return cls(route_name_column, measure_column, from_measure_column, to_measure_column)


class MapServiceLayer:
    display_name: str
    geometry_type: str
    system_columns: SystemColumns
    feature_class: str
    can_export: bool

    def __init__(self, display_name: str, geometry_type: str, system_columns: SystemColumns, feature_class: str, can_export: bool) -> None:
        self.display_name = display_name
        self.geometry_type = geometry_type
        self.system_columns = system_columns
        self.feature_class = feature_class
        self.can_export = can_export

    @classmethod
    def from_json(cls, data: dict):
        display_name = data["displayName"]
        geometry_type = data["geometryType"]
        system_columns = SystemColumns.from_json(data["systemColumns"])
        feature_class = data["featureClass"]
        can_export = data["canExport"]
        return cls(display_name, geometry_type, system_columns, feature_class, can_export)

class StaticLayerItem:
    id: str
    name: str
    category_id: str
    mapservice_layers: MapServiceLayer

    def __init__(self, id: str, name: str, category_id: str, mapservice_layers: MapServiceLayer) -> None:
        self.id = id
        self.name = name
        self.category_id = category_id
        self.mapservice_layers = mapservice_layers
    
    @classmethod
    def from_json(cls, data: dict):
        id = data["id"]
        name = data["name"]
        category_id = data["categoryId"]
        mapservice_layers = MapServiceLayer.from_json(data["mapServiceLayers"])
        return cls(id, name, category_id, mapservice_layers)