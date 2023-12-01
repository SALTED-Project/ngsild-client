import setuptools

setuptools.setup(
    name='ngsildclient',
    version='0.1',
    description='An NGSI-LD python client package',
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=['multipledispatch','pandas','scalpl','geojson'],
)
