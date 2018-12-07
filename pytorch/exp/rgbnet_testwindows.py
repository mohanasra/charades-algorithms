#!/usr/bin/env python
import sys
#sys.path.insert(0, '..')
sys.path.insert(0, '.')
from main import main

args = [
    '--name', "/" + __file__.split('\\')[-1].split('.')[0],  # name is filename
    '--print-freq', '1',
    '--dataset', 'charadesrgb',
    '--data', 'C:/code/git/forks/charades-algorithms/datasets/small/Charades_v1_rgb',
    '--arch', 'vgg16',
    '--lr', '1e-3',
    '--batch-size', '1',
    '--train-size', '0.1',
    '--val-size', '0.1',
    '--cache-dir', 'temp/gsigurds/ai2/caches/',
    '--pretrained',
    '--pretrained-weights', '../datasets/twostream_rgb.pth.tar',
    '--workers', 0,
    '--evaluate',
]
sys.argv.extend(args)
main()
