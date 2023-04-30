###################################
# Author: Kudzai Richard Jaure
# Email: krjaure556@gmail.com
###################################
import os
import torch
import sys

class BaseModel(torch.nn.Module):
    def name(self):
        return 'BaseModel'

    def __init__(self, opt):
        super().__init__()
        self.opt = opt
        self.gpu_ids = opt.gpu_ids
        self.isTrain = opt.isTrain
        self.device = torch.device('cuda' if torch.cuda.is_available() and self.gpu_ids else 'cpu')
        self.save_dir = os.path.join(opt.checkpoints_dir, opt.name)

    def set_input(self, input):
        self.input = input

    def forward(self):
        pass

    # used in test time, no backprop
    def test(self):
        pass

    def get_image_paths(self):
        pass

    def optimize_parameters(self):
        pass

    def get_current_visuals(self):
        return self.input

    def get_current_errors(self):
        return {}

    def save(self, label):
        pass
    
    # helper saving function that can be used by subclasses

    def save_network(self, network, network_label, epoch_label):
        save_filename = f'{epoch_label}_net_{network_label}.pth'
        save_path = os.path.join(self.save_dir, save_filename)
        torch.save(network.to('cpu').state_dict(), save_path)
        network.to(self.device)

    def save_optim(self, optim, network_label, epoch_label):
        save_filename = f'{epoch_label}_optim_{network_label}.pth'
        save_path = os.path.join(self.save_dir, save_filename)
        torch.save(optim.state_dict(), save_path)


    # helper loading function that can be used by subclasses
def load_network(self, network, network_label, epoch_label, save_dir=''):
    save_filename = f'{epoch_label}_net_{network_label}.pth'
    if not save_dir:
        save_dir = self.save_dir
    save_path = os.path.join(save_dir, save_filename)
    if not os.path.isfile(save_path):
        print(f'{save_path} does not exist yet!')
        if network_label == 'G':
            raise Exception('Generator must exist!')
    else:
        try:
            network.load_state_dict(torch.load(save_path))
        except:
            pretrained_dict = torch.load(save_path)
            model_dict = network.state_dict()
            try:
                pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict}
                network.load_state_dict(pretrained_dict)
                if self.opt.verbose:
                    print(f'Pretrained network {network_label} has excessive layers; Only loading layers that are used')
            except:
                print(f'Pretrained network {network_label} has fewer layers; The following are not initialized:')
                for k, v in pretrained_dict.items():
                    if v.size() == model_dict[k].size():
                        model_dict[k] = v


                not_initialized = set()
                for k, v in model_dict.items():
                    if k not in pretrained_dict or v.size() != pretrained_dict[k].size():
                        not_initialized.add(k.split('.')[0])

                print(sorted(not_initialized))
                network.load_state_dict(model_dict)
                
        network.to(self.device)

    # helper loading function that can be used by subclasses
    def load_optim(self, network, network_label, epoch_label, save_dir=''):        
        save_filename = '%s_optim_%s.pth' % (epoch_label, network_label)
        if not save_dir:
            save_dir = self.save_dir
        save_path = os.path.join(save_dir, save_filename)        
        if not os.path.isfile(save_path):
            print('%s not exists yet!' % save_path)
            if network_label == 'G':
                raise('Generator must exist!')
        else:
            #network.load_state_dict(torch.load(save_path))
            try:
                network.load_state_dict(torch.load(save_path, map_location=torch.device("cpu")))
            except:   
                pretrained_dict = torch.load(save_path, map_location=torch.device("cpu"))                
                model_dict = network.state_dict()
                try:
                    pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict}                    
                    network.load_state_dict(pretrained_dict)
                    if self.opt.verbose:
                        print('Pretrained network %s has excessive layers; Only loading layers that are used' % network_label)
                except:
                    print('Pretrained network %s has fewer layers; The following are not initialized:' % network_label)
                    for k, v in pretrained_dict.items():                      
                        if v.size() == model_dict[k].size():
                            model_dict[k] = v

                    not_initialized = set()
                   

                    for k, v in model_dict.items():
                        if k not in pretrained_dict or v.size() != pretrained_dict[k].size():
                            not_initialized.add(k.split('.')[0])
                    
                    print(sorted(not_initialized))
                    network.load_state_dict(model_dict)
                   
        network.to(self.device)

    def update_learning_rate():
        pass
