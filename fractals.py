import argparse
import subprocess
import os

if os.name == 'posix':
    isPosix = True

WORK_DIR = os.environ['PWD']
DISPLAY_POSIX = ("xdg-open ")
DISPLAY_WIN = ("C:\\Windows\\System32>rundll32.exe")
DICO_ARGS = {"b" : "/brocoli/",
             "m" : "/mandelbrot/",
             "s" : "/sponge/",
             "v" : "/high-voltage/"}
DICO_ARGS_WIN = {"b" : "\\brocoli\\",
             "m" : "\\mandelbrot\\",
             "s" : "\\sponge\\",
             "v" : "\\high-voltage\\"}

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--brocoli", help="shows an image of the brocoli set",
                    action="store_const", const="b")
parser.add_argument("-m", "--mandelbrot", help="shows an image of the mandelbrot set",
                    action="store_const", const="m")
parser.add_argument("-s", "--sponge", help="shows an image of the menger's sponge",
                    action="store_const", const="s")
parser.add_argument("-v", "--voltage", help="shows an image of a fractal piece of glass after high voltage",
                    action="store_const", const="v")
parser.add_argument("-f", "--format", type = str, choices=["jpg","png"], default="jpg",
                    help="Choose the format from jpg, png...")
args = parser.parse_args()
barg = args.brocoli
marg = args.mandelbrot
sarg = args.sponge
varg = args.voltage
farg = args.format

def display(dict_args, argument, image_format, display):
    """ """
    path = DISPLAY_POSIX + WORK_DIR + dict_args[argument]
    subprocess.call(path + "image." + image_format, shell=True)

def condition_image(unix_like):
    if unix_like:
        dico = DICO_ARGS
        disp = DISPLAY_POSIX
    else:
        dico = DICO_ARGS_WIN
        disp = DISPLAY_WIN
    
    if barg == "b":
        display(dico, barg, farg, disp)
    if marg =="m":
        display(dico, marg, farg, disp)
    if sarg == "s":
        display(dico, sarg, farg, disp)
    if varg == "v":
        display(dico, varg, farg, disp)

def condition_format(unix_like):
    if farg == "jpg":
        condition_image(unix_like)

    if farg == "png":
        condition_image(unix_like)
    
if isPosix:
    condition_format(isPosix)
else:
    condition_format(isPosix)


