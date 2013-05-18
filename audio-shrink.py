from optparse import OptionParser
import os, shlex, subprocess

parser = OptionParser()
parser.add_option('-i', '--input', dest='fInput')
parser.add_option('-o', '--output', dest='fOutput')
(options, args) = parser.parse_args()

inputDir = options.fInput
outputDir = options.fOutput

if not outputDir.endswith("/"):
    outputDir += "/"

def extractCurrentDirectory(dir):
    return dir.replace(inputDir, "").replace("/", "", 1)

for root, dirs, files in os.walk(inputDir):
    root = extractCurrentDirectory(root)

    # Create the child directory if it doesn't exist so we can put files in it
    if not os.path.exists(outputDir + root):
        os.makedirs(outputDir + root)

    for name in files:
        if name.endswith(".flac"):
            print("Found File: %s" % name)
            command = shlex.split("ffmpeg -i \"%s\" -f ogg -c:a libvorbis -q 8 -map 0:0 \"%s\"" % (os.path.abspath(name), outputDir + root + "/" + name))
            p = subprocess.call(command)
