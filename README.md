<h3>Synthetic rain generator</h3>
Adds synthetic rain to images, saves them in the same folder with \_rain added to the end of the filename(s). If one or more parameters are not given, they will be randomized to reasonable values for each image.

<h4>Usage</h4>
raingen.py -i <inputfiles> -a <angle> -l <length> -t <thickness> -n <drop_nrs>

<h4>Example</h4>
python raingen.py -i imgs/*.jpg -a 10 -l 30 -t 2 -n 1000

<h4>Arguments</h4>
-i Can be given several filenames separated by comma or generated with wildcard *
-a Angle given as integer between -90 and 90
-l The max length of rain drops in pixels (the actual length is random up to length), should be matched somehow to the image resolution
-t Rain drop width
-n Number of raindrops to be added

<h4>Dependencies</h4>
* opencv
* numpy