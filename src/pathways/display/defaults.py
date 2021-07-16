
from ..io.pathways_frame import PathwaysFrame

from IPython.core.display import display, HTML

def display_info(df: PathwaysFrame):
    info = df.get_pathways_info()
    html_str = f"""<li>Dataset Type:{str(info.dataset_type.value)}</li>
    <li>Geometry:{info.dataset_info.mapservice_layers.geometry_type}</li>"""
    if info.dataset_info.mapservice_layers.geometry_type == 'LrsPoint':
        html_str += f'<li>RouteName Column:{str(info.dataset_info.mapservice_layers.system_columns.route_name_column)}</li>'
        html_str += f'<li>Measure Column:{str(info.dataset_info.mapservice_layers.system_columns.measure_column)}</li>'
    
    if info.dataset_info.mapservice_layers.geometry_type == 'LrsLine':
        html_str += f'<li>RouteName Column:{str(info.dataset_info.mapservice_layers.system_columns.route_name_column)}</li>'
        html_str += f'<li>From Measure Column:{str(info.dataset_info.mapservice_layers.system_columns.from_measure_column)}</li>'
        html_str += f'<li>To Measure Column:{str(info.dataset_info.mapservice_layers.system_columns.to_measure_column)}</li>'
    html_str = f'<ul>{html_str}</ul>' 
    display(HTML(html_str))