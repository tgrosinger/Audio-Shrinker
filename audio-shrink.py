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
        if name.endswith(".flac"):
            print("Transcoding File: %s" % name)
            output = replace_last((outputDir + root + "/" + name), "flac", "ogg")
            command = shlex.split("ffmpeg -i \"%s\" -f ogg -c:a libvorbis -q 8 -map 0:0 \"%s\"" % (name, output))
            p = subprocess.call(command)
