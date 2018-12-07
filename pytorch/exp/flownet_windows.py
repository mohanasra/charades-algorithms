#!/usr/bin/env python
import sys
#sys.path.insert(0, '..')
sys.path.insert(0, '.')
from main import main

args = [
    '--name', "/" + __file__.split('\\')[-1].split('.')[0],  # name is filename
    '--print-freq', '1',
    '--dataset', 'charadesflow',
    '--arch', 'vgg16flow',
    '--data','../datasets/Charades_v1_flow/',
    '--lr', '5e-3',
    '--lr-decay-rate','15',
    '--epochs','40',
    '--batch-size', '8',
    '--train-size', '0.2',
    '--val-size', '0.001',
    '--cache-dir', 'temp/gsigurds/ai2/caches/',
    '--pretrained',
    '--pretrained-weights', '../datasets/vgg16flow_ucf101.pth',
#     '--resume', './twostream_flow.pth',
    '--evaluate',
]
sys.argv.extend(args)
main()
