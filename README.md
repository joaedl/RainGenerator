#Synthetic rain generator
Adds synthetic rain to images, saves them in the same folder with \_rain added to the end of the filename(s). If one or more parameters are not given, they will be randomized to reasonable values for each image.

![Image of generated rain]
(https://github.com/joaedl/RainGenerator/blob/master/street_rain.jpg)

###Usage
raingen.py -i <inputfiles> -a <angle> -l <length> -t <thickness> -n <drop_nrs>

###Example
python raingen.py -i imgs/*.jpg -a 10 -l 30 -t 2 -n 1000

###Arguments
-i Can be given several filenames separated by comma or generated with wildcard *
-a Angle given as integer between -90 and 90
-l The max length of rain drops in pixels (the actual length is random up to length), should be matched somehow to the image resolution
-t Rain drop width
-n Number of raindrops to be added

###Dependencies
* opencv
* numpy