import re
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.datasets import load_svmlight_file


class SvmlightParser:
    def __init__(self, filepath, tail=None):
        self.filepath = filepath
        self.tail = tail

    def __call__(self):
        with open(self.filepath, "rb") as fp:
            infoline = fp.readline()
            infoline = re.sub(r"^b'", "", str(infoline))
            n_features = int(re.sub(r"^\d+\s(\d+)\s\d+.*$", r"\1", infoline))
            features, labels = load_svmlight_file(
                fp, n_features=n_features, multilabel=True
            )
        mlb = MultiLabelBinarizer()
        labels = mlb.fit_transform(labels)
        features = np.array(features.todense())
        features = np.ascontiguousarray(features)
        if self.tail is None:
            return features, labels
        else:
            return features[-self.tail:], labels[-self.tail:]
