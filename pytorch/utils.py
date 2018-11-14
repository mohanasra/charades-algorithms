import cPickle as pickle
import csv
import argparse
import os


def parse():
    print('parsing arguments')
    parser = argparse.ArgumentParser(description='Utils...')
    parser.add_argument('--operation', default='test', type=str)
    
    args = parser.parse_args()
    print("Arguments: {}".format(args))
    
    return args

def reduce_charades_csv(inputFile, outputFile):
    reducedSet = []
    with open(inputFile) as f:
        reader = csv.DictReader(f)
        i = 1
        for row in reader:
            if(row['scene'] == 'Garage'):
                 print("Row {} - {}".format(i, row))
                 reducedSet.append(row)
                 i += 1
        
    with open(outputFile, 'wb') as smallFile:
        print("Saving result to '%s'" % outputFile)
        fieldnames = ['id','subject','scene','quality','relevance','verified','script','objects','descriptions','actions','length']
        writer = csv.DictWriter(smallFile, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()
        writer.writerows(reducedSet)
            


def main():
    global opt
    opt = parse()
    print(vars(opt))
#     reduce_charades_csv('./datasets/Charades/Charades_v1_train.csv', './datasets/Charades/Charades_v1_train_small.csv')
    reduce_charades_csv('./datasets/Charades/Charades_v1_test.csv', './datasets/Charades/Charades_v1_test_small.csv')


if __name__ == '__main__':
    main()
