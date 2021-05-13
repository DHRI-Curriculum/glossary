# GIS

## Glossary  

Please see below a list of key terms and concepts, provided in alphabetical order, from Javier Otero Peña's [Introduction to Mapping using QGIS workshop](https://github.com/DHRI-Curriculum/mapping) as well as Olivia Ildefonso's Introduction to Making an Interactive Map workshop.

An *attribute* is a characteristic of a feature (see below). Attributes can contain data of different types: strings (text), numerical values, dates, or booleans. Each column in the Attribute Table represents a different attribute.

*attribute type* Attributes can be stored as different data types, including strings (text), integer, double, dates, and booleans.

*color ramp* provides a range of color to the features of a map layer based on an attribute from the layer. 

*Feature*: a visual element on a map. For vector data it's the points, lines and polygons. Each individual feature (each point, each line, and each polygon) is represented as a row in the attribute table. 

*Georeferencing*: the process of using geographic data to represent features on a GIS.

*Geocoding* is a spatial process that uses a *geographic address locator* to match addresses with location coordinates and create a point layer. It turns a text file (e.g. CSV) into a vector file (e.g. points layer).

*Layers* are "containers" of the data in QGIS. On the map view, layers can be imagined as transparent film sheets that are laid one over another. With the exception of raster layers, each layer contains an Attribute Table, that is, a series of features that in turn have their own attributes. Vector layers can only contain one type of vectors, be it: points, lines or polygons.

*Polygon*: a figure with three or more sides. In GIS, it usually refers to complex areas outlining lakes, city blocks, a set of buildings, or other complex features of the map, that can be outlined using interconnected points. A polygon can have an unlimited amount of points. The more points (or "higher the resolution"), the smoother the polygon will look to the human eye.

*Raster*: images of a specific location that represent visually continuous data such as temperature and elevation at a given resolution. Higher resolutions mean more precision but also larger file size. Raster layers have no Attribute Table; the values are stored within the image and represented as different hues or colors. Raster images can also be used for reference or aesthetic purposes (e.g. satellite photos).

*Resolution*: the scale at which the data is aggregated and displayed. For raster data this will be the size of the pixel. For vector data it is referring to the scale or mapping unit (e.g. neighborhood level, city level, state level, etc).

*Shapefile*: There are two types of geographic data--vector data (points, lines, and polygons) and raster data (pixels). The most common way that vector data is stored is in the format of a shapefile. Therefore, a shapefile is a file type that stores vector data.

*Spatial Join*: A Spatial join is a GIS operation that affixes data from one feature layer's attribute table to another from a spatial perspective. Spatial joins begin by selecting a target feature and comparing it spatially to other feature layers. There are two types of spatial joins--*spatial join by attribute* and *spatial join by location*. Both of them are ways that the mapping software will let you add data from one map layer or file to another map layer. A *spatial join by attribute* is used when you want to join non-spatial data, such as a text file, to spatial data, such as a shapefile. A *spatial join by location* is used when you want to join two layers of spatial data (e.g. a points layer to a polygon layer). 

*Spatial join by attribute* is based on adding the attributes from one layer to another based on a shared attribute or variable.

*Spatial Join by location* is when you have two shapefiles that you want to combine based on where the features are located on the map. For example if you have a map of US states and you want to add information about its cities, you can run a spatial join by location.

*Vector*: a scalable point, line or polygon that can be easily created, edited, or deleted using GIS. Does not have a specific resolution. In QGIS, vectors are contained in vector layers, that can only contain a single type of vectors. Each vector represents a single feature, although some features may be represented by more than one vector (e.g. the vector of the United States includes the mainland U.S. polygon but also polygons for Alaska and Hawaii).
