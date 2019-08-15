ssh-keygen -t rsa -b 4096 -C "bryan.orourke24@gmail.com"
cat ~/.ssh/id_rsa.pub

git clone https://github.com/borourke/retinanet-sample.git
cd retinanet-sample

curl -L https://github.com/fizyr/keras-retinanet/releases/download/0.5.1/resnet50_coco_best_v2.1.0.h5 --output resnet50_coco_best_v2.1.0.h5

retinanet-train --weights resnet50_coco_best_v2.1.0.h5 --batch-size 8 --steps 7248 --epochs 20 --snapshot-path snapshots --tensorboard-dir tensorboard csv dataset/train.csv dataset/classes.csv

# To convert the model
retinanet-convert-model <path/to/desired/snapshot.h5> <path/to/output/model.h5>

# To evaluate the model
retinanet-evaluate <path/to/output/model.h5> csv <path/to/train.csv> <path/to/classes.csv>


