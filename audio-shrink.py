from optparse import OptionParser
import os
import shlex
import subprocess
import sys


usage = "usage: %prog -i <input dir> -o <output dir> [options]"
parser = OptionParser(usage=usage)
parser.add_option('-i', '--input', dest='fInput', help='Required, Directory to scan for media files')
parser.add_option('-o', '--output', dest='fOutput', help='Required, Directory to output transcoded files')
parser.add_option('-f', '--inputFormat', dest='inFormat', default='flac',
                  help='Format of file to look for in input directory')
(options, args) = parser.parse_args()

inputDir = options.fInput
outputDir = options.fOutput

if len(inputDir) == 0 or len(outputDir) == 0:
    parser.print_help()
    sys.exit(1)

if not outputDir.endswith("/"):
    outputDir += "/"


def extractCurrentDirectory(dir):
    return dir.replace(inputDir, "").replace("/", "", 1)


def replace_last(source_string, replace_what, replace_with):
    head, sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail


for root, dirs, files in os.walk(inputDir):
    os.chdir(root)
    root = extractCurrentDirectory(root)

    # Create the child directory if it doesn't exist so we can put files in it
    if not os.path.exists(outputDir + root):
        os.makedirs(outputDir + root)

    for name in files:
        if name.endswith(".%s" % options.inFormat):
            print("Transcoding File: %s" % name)
            output = replace_last((outputDir + root + "/" + name), "flac", "ogg")
            command = shlex.split("ffmpeg -i \"%s\" -f ogg -c:a libvorbis -q 5 -map 0:0 \"%s\"" % (name, output))
            p = subprocess.call(command)
