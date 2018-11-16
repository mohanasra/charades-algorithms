#!/usr/bin/env python
import sys
#sys.path.insert(0, '..')
sys.path.insert(0, '.')
from main import main

args = [
    '--name', "/" + __file__.split('\\')[-1].split('.')[0],  # name is filename
    '--print-freq', '1',
    '--dataset', 'charadesrgb',
    '--arch', 'vgg16',
    '--lr', '1e-3',
    '--batch-size', '1',
    '--workers', '0',
    '--train-size', '0.1',
    '--val-size', '0.1',
    '--cache-dir', 'c:/Temp/charades_cache',
    '--data', 'C:/code/git/forks/charades-algorithms/datasets/small/Charades_v1_rgb',
#     '--inputsize', '112',
    '--train-file', './datasets/Charades/Charades_v1_train_small.csv',
    '--val-file', './datasets/Charades/Charades_v1_test_small.csv',
    '--pretrained',
    #'--evaluate',
]
sys.argv.extend(args)
main()
