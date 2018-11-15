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
            

def gen_script_make_small_db(inputFile, outputPath, dataKind):
    shFileName = "{}/make_small_{}_db.sh".format(outputPath, dataKind)
    with open(inputFile) as srcFile, open(shFileName, "wx") as destFile:
        reader = csv.DictReader(srcFile)
        for row in reader:
            shcmd = "cp Charades_v1_480/{}.mp4 {}/videos/\n".format(row['id'], outputPath)
            destFile.write(shcmd)
            shcmd = "cp -r Charades_v1_rgb/{} {}/rgb/\n".format(row['id'], outputPath)
            destFile.write(shcmd)
#             shcmd = "cp -r Charades_v1_rgb/{} small/videos/".format(row['id'])
#             cmdLns.append(shcmd)
            
    print("gen_script_make_small_db completed")

def main():
    global opt
    opt = parse()
    print(vars(opt))
#     reduce_charades_csv('./datasets/Charades/Charades_v1_train.csv', './datasets/Charades/Charades_v1_train_small.csv')
#     reduce_charades_csv('./datasets/Charades/Charades_v1_test.csv', './datasets/Charades/Charades_v1_test_small.csv')
    gen_script_make_small_db('./datasets/Charades/Charades_v1_train_small.csv', '/home/mohana.r/data/code/git/charades-algorithms/datasets/small', 'train')
    gen_script_make_small_db('./datasets/Charades/Charades_v1_test_small.csv', '/home/mohana.r/data/code/git/charades-algorithms/datasets/small', 'test')


if __name__ == '__main__':
    main()
