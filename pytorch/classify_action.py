import operator

def load_epoch_result(epoch_result_file):
    epoch_data = {}
    with open(epoch_result_file) as epoch_results:
        for line in epoch_results:
            epoch_data = {}
            values = line.split(" ")
            id = values[0]
            values = values[1:]
            looping = 0
            for entry in values:
                epoch_data[looping] = float(values[looping]) 
                looping += 1
#             key_max = max(epoch_data.keys(), key=(lambda k: epoch_data[k]))
#             top5 = dict(sorted(epoch_data.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
            top5 = sorted(epoch_data.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]
#             top5 = sorted(top5.iteritems(), key=operator.itemgetter(1), reverse=True) 
#             print('id - {}, top5 - {}'.format(id, top5))
        return top5

def print_epoch_result(epoch_result_file, charades_classes):
    epoch_data = {}
    with open(epoch_result_file) as epoch_results:
        for line in epoch_results:
            epoch_data = {}
            values = line.split(" ")
            id = values[0]
            values = values[1:]
            looping = 0
            actions = ""
            for entry in values:
                epoch_data[looping] = float(values[looping]) 
                looping += 1
            top5 = sorted(epoch_data.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]
            for classification_result in top5:
                actions += "\t{}\n".format(charades_classes[classification_result[0]])
            print("\nFollowing are top 5 actions identified in video with id {}...\n".format(id))
            print(actions)


def load_charades_classes(charades_classes_file):
    charades_classes = {}
    with open(charades_classes_file) as input_file:
        for line in input_file:
            charades_class_tuple = line.split(";")
            charades_classes[int(charades_class_tuple[0])] = charades_class_tuple[1]
            
        return charades_classes
    return None
        
def main():
    charades_classes = load_charades_classes('/home/mohana.r/data/code/git/charades-algorithms/pytorch/datasets/Charades/Charades_v1_classes_new.txt')
#     print("charades classes - {}".format(charades_classes))
    print_epoch_result('temp/gsigurds/ai2/caches/rgbnet_test/epoch_000.txt', charades_classes)


if __name__ == '__main__':
    main()
