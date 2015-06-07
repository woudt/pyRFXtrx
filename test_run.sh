#!/bin/sh

python -m doctest -v doctest/lighting.txt
python -m doctest -v doctest/lowlevel.txt

# run all again without the -v verbose options, to show all errors at the end
python -m doctest doctest/lighting.txt
python -m doctest doctest/lowlevel.txt
