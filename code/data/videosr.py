import os
import glob
from data import videodata


class VIDEOSR(videodata.VIDEODATA):
    def __init__(self, args, name='CDVL_VIDEO', train=True):
        super(VIDEOSR, self).__init__(args, name=name, train=train)

    def _set_filesystem(self, dir_data):
        print("Loading {} => {} DataSet".format("train" if self.train else "test", self.name))
        self.apath = dir_data
        self.dir_gt = self.apath
        self.dir_input = self.apath
        print("DataSet gt path:", self.dir_gt)
        print("DataSet blur path:", self.dir_input)
