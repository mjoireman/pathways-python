### Pathways Python Library

Python Package for integrating pathways platform dataset into data science workflow

#### Features
- Authenticate using existing pathways credentials
- List the datasets in pathways
- Read pathways datasets into geopandas dataframes
- integrate seamlessly with open source datascience toolchain
- Jupyter widgets to improve data scientist experience 
    - view the list of datasets
    - inspect the metadata
- Python typings to improve python development experience
- package distributed via pip package manager
- works well with jupyter notebooks and jupyter lab


### Use cases
- ideal for data preperation since it always gets the latest dataset from pathways
- used to create ETL jobs to move the prepared datasets to other systems
- data scientist can perfrom exploratory analysis to better understand the data


### High level Design


### API Design
- authentication(username, password, url<optional>)
- io
    - read_dataset(id, dataset_type) -> geodataframe
- widgets
    - display()
        - view list of datasets
        - view metadata of dataset
    - progress for data downloader
- datasets
    - list()
        - static
        - managed
        - studies
        - recommendations
    - query


### Optimizations
- scalable and fast data retrival
- query optimizations using columnar data storage format
- zip compression to compress dataset to reduce the bandwidth requirement  


### Continuous Delivery Pipeline
- codebuild 
    - run unit test cases
    - version the build
    - deploy to pip package manager

### Limitations
- Entire dataset needs to fit into in-memeory
- pathways datasets will be updated contantly and schema for static data will change if original data provider decided to update the dataset


### Dependency 
- geopandas
- pandas
- pyarrow
- fiona 

### Getting Started

- Packages for data scientist
``` bash
conda create -n pathways-ds -y
conda activate pathways-ds
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install python=3 geopandas pyarrow rtree pyproj ipykernel seaborn jupyterlab -y
pip3 install cartoframes
pip3 install https://map-resources.vdotp4p.com/python/pathways.zip
```

```
cd <notebook folder>
jupyter notebook
```

``` bash
conda remove --name pathways-ds --all -y
```

- Packages for data engineer

``` bash
conda create -n pathways-de -y
conda activate pathways-de
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install python=3 geopandas pyarrow rtree pyproj -y
pip3 install https://map-resources.vdotp4p.com/python/pathways.zip

```

stop metrics collection

``` python
cartoframes.utils.setup_metrics(False)
```

Setting Credentials 

``` python
from pathways_client.auth import set_default_credentials

set_default_credentials('creds.json')
```
creds.json file contents
``` json
{
    "username": "",
    "password": "",
    "base_url": "https://api.vdotpathways-dev.com"
}
```
