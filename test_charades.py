from vocab import Vocabulary
import evaluation_charades as evaluation
DATA_PATH = '/content/Weak_Supervised_Moment/Data/'
# RUN_PATH = '/home/usr/python/weak_supervised_video_moment/runs/'

evaluation.evalrank("/content/Weak_Supervised_Moment/Model/test_charades/model_best.pth.tar", data_path=DATA_PATH, split="test")
