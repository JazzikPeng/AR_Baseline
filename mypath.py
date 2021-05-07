
class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'ucf101':
            # folder that contains class labels
            root_dir = '/home/mindmaster/Projects/cs231n/ar_project/datasets/UCF101/UCF-101'

            # Save preprocess data into output_dir
            output_dir = '/home/mindmaster/Projects/cs231n/ar_project/datasets/UCF101/ucf101'

            return root_dir, output_dir
        elif database == 'hmdb51':
            # folder that contains class labels
            root_dir = '/Path/to/hmdb-51'

            output_dir = '/path/to/VAR/hmdb51'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        return '/home/mindmaster/Projects/cs231n/ar_project/weights/c3d-pretrained.pth'