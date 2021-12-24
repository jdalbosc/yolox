# -*- coding: utf-8 -*-
import os
from absl import app, flags
from pathlib import Path
import cv2

flags.DEFINE_string('output', '', 'path to output label file')
flags.DEFINE_string('dataset', '', 'path to coco128 dataset directory')
FLAGS = flags.FLAGS

def read_image_size(image_path):
    img = cv2.imread(str(image_path))
    (h, w) = img.shape[:2]
    return w, h

def read_image_labels(label_dir_path, image_file_path):
    label_file_path = Path(label_dir_path).joinpath(f'{image_file_path.stem}.txt')    
    with open(label_file_path) as label_file:
        labels = []
        while True:
            label_line = label_file.readline()
            if not label_line:
                break
            label_strings = label_line.split()
            label_values = []
            for i in range(5):
                if i == 0:
                    label_values.append(int(label_strings[i]))
                else:
                    label_values.append(float(label_strings[i]))
            labels.append(label_values)

    return labels

def main(_argv):
    output_file_path = FLAGS.output
    dataset_path = FLAGS.dataset
    image_dir_path = os.path.join(dataset_path, 'images', 'train2017')
    label_dir_path = os.path.join(dataset_path, 'labels', 'train2017')

    with open(output_file_path, 'w') as output_file:        
        for image_file_path in Path(image_dir_path).glob('**/*.jpg'):
            labels = read_image_labels(label_dir_path, image_file_path)
            w, h = read_image_size(image_file_path)
            output_file.write(str(image_file_path.resolve()))
            for label in labels:
                object_x_center = float(label[1])
                object_y_center = float(label[2])
                object_width = float(label[3])
                object_height = float(label[4])
                object_x_tl = int((object_x_center - object_width/2) * w)
                object_y_tl = int((object_y_center - object_height/2) * h)
                object_x_br = int((object_x_center + object_width/2) * w)
                object_y_br = int((object_y_center + object_height/2) * h)
                object_label = label[0]
                output_file.write(f' {object_x_tl},{object_y_tl},{object_x_br},{object_y_br},{object_label}')
            output_file.write("\n")

if __name__ == '__main__':
    app.run(main)



