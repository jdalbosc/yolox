# -*- coding: utf-8 -*-
import os
from absl import app, flags
from pathlib import Path
import fiftyone as fo


flags.DEFINE_string('dataset', '', 'path to coco128 dataset directory')
FLAGS = flags.FLAGS

def open_fifty_one():
    dataset = fo.Dataset.from_dir(
        dataset_dir=Path(FLAGS.dataset).resolve(),
        dataset_type=fo.types.YOLOv5Dataset,
        name='coco-128',
    )
    
    # View summary info about the dataset
    print(dataset)

    # Print the first few samples in the dataset
    print(dataset.head())

    session = fo.launch_app(dataset)
    session.wait()

def main(_argv):
    open_fifty_one()

if __name__ == '__main__':
    app.run(main)



