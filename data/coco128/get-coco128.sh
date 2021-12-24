kaggle datasets download -d ultralytics/coco128
unzip coco128.zip
python3 ./create_yolox_labels.py --dataset=coco128 --output=full.txt
cat full.txt | head -n 118 > train.txt
cat full.txt | tail -n 10 > val.txt
