"""
Initialize the model module
New models can be defined by adding scripts under models/
"""
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.distributed as dist
import torchvision.models as tmodels
import importlib


def create_model(args):
#     for m in tmodels.__dict__:
#         print(m)
    if args.arch in tmodels.__dict__:  # torchvision models
        if args.pretrained:
            print("=> using pre-trained model '{}'".format(args.arch))
            model = tmodels.__dict__[args.arch](pretrained=True)
            model = model.cuda()
        else:
            print("=> creating model '{}'".format(args.arch))
            model = tmodels.__dict__[args.arch]()
    else:  # defined as script in this directory
        model = importlib.import_module('.'+args.arch, package='models').model
        if not args.pretrained_weights == '':
            print('loading pretrained-weights from {}'.format(args.pretrained_weights))
            model.load_state_dict(torch.load(args.pretrained_weights))

    print(model)
    # replace last layer
    if hasattr(model, 'classifier'):
        print("=> Model has classifier")
        newcls = list(model.classifier.children())
        newcls = newcls[:-1] + [nn.Linear(newcls[-1].in_features, args.nclass).cuda()]
        model.classifier = nn.Sequential(*newcls)
    elif hasattr(model, 'fc'):
        print("=> Model has fc")
        model.fc = nn.Linear(model.fc.in_features, args.nclass)
        if hasattr(model, 'AuxLogits'):
            model.AuxLogits.fc = nn.Linear(model.AuxLogits.fc.in_features, args.nclass)
    else:
        print("=> Model does not have classifier & fc")
        newcls = list(model.children())[:-1]
        newcls = list(model.children())
        lastSeq = list(*newcls[-1::1])
#         print(len(lastSeq))
#         print(lastSeq)
        lastLinear = lastSeq[1]
#         print(lastLinear)
        newLinear = nn.Linear(lastLinear.in_features, args.nclass).cuda()
        lastSeq[1] = newLinear
        newLastSeq = [nn.Sequential(*lastSeq)]
        newcls = newcls[:-1] + newLastSeq
#         newcls = newcls[:-1] + [nn.Linear(lastLinear.in_features, args.nclass).cuda()]
        model = nn.Sequential(*newcls)

    if args.distributed:
        dist.init_process_group(backend=args.dist_backend, init_method=args.dist_url,
                                world_size=args.world_size)
        model.cuda()
        model = torch.nn.parallel.DistributedDataParallel(model)
    else:
        if hasattr(model, 'features'):
            model.features = torch.nn.DataParallel(model.features)
            model.cuda()
        else:
            model = torch.nn.DataParallel(model).cuda()

    # define loss function and optimizer
    criterion = nn.CrossEntropyLoss().cuda()
    optimizer = torch.optim.SGD(model.parameters(), args.lr,
                                momentum=args.momentum,
                                weight_decay=args.weight_decay)
    cudnn.benchmark = True
    return model, criterion, optimizer
