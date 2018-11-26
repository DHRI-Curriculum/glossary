# GIS

## Glossary  

Please see below a list of key terms and concepts, provided in alphabetical order, from Javier Otero Peña's [Introduction to Mapping using QGIS workshop](https://github.com/DHRI-Curriculum/mapping).

An *attribute* is a characteristic of a feature (see below). Attributes can contain data of different types: strings (text), numerical values, dates, or booleans. Each column in the Attribute Table represents a different attribute.

*Feature*: an element that appears in a layer and typically has attributes. Each row in the Attribute Table represents a different feature. Each feature can be represented on a map by one (or more) vectors, be it points, lines or polygons.

*Georeferencing*: the process of using geographic data to represent features on a GIS.

*Layers* are "containers" of the data in QGIS. On the map view, layers can be imagined as transparent film sheets that are laid one over another. With the exception of raster layers, each layer contains an Attribute Table, that is, a series of features that in turn have their own attributes. Vector layers can only contain one type of vectors, be it: points, lines or polygons.

*Raster*: images of a specific location that represent visually continuous data such as temperature and elevation at a given resolution. Higher resolutions mean more precision but also larger file size. Raster layers have no Attribute Table; the values are stored within the image and represented as different hues or colors. Raster images can also be used for reference or aesthetic purposes (e.g. satellite photos).

*Vector*: a scalable point, line or polygon that can be easily created, edited, or deleted using QGIS. Does not have a specific resolution.
