Audio-Shrinker
==============

After a bit of reasearch I have determined that OGG Vorbis is the best format to use for audio on mobile devices. It has excellent compression with great quality even at lower bit rates. To simplify the process of comverting my music, this small app will take an input directory and convert the contained audio files using mmpeg.

Installation
------------

~~~
# Install some dependencies
sudo apt-get install build-essential vorbis-tools git autoconf automake libvorbis-dev
 
# If ffmpeg is installed, remove it
sudo apt-get remove ffmpeg
 
# Now install the new version
cd /opt
sudo git clone git://source.ffmpeg.org/ffmpeg.git ffmpeg
sudo ./configure --enable-libvorbis
sudo make
sudo make install
~~~

Detailed installation instructions can be found in [this blog post](http://tostring.co/audio-transcoding-made-slightly-easier/).

Usage
-----

A simple help command is included:

~~~
python audio-shrink.py -h
~~~

To convert a directory of files:

~~~
python audio-shrink.py -i <input dir> -o <output dir> -f <input format>
~~~

The input directory structure will be mirrored in the output directory. For example, album folders will be created if you point the script at an artist folder.
