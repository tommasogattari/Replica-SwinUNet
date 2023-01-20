[Here](https://drive.google.com/file/d/15tIdXrgodIMF--DXQd9r1rT_QXZGKFK6/view?usp=sharing?h50) you can find all folders and files needed to run the whole project

In the image below there is the scructure of the project:
![preprocessing data](https://user-images.githubusercontent.com/48884211/213570250-dff7abcf-0926-4cf9-a976-1d0a7ec99c94.jpg)

In the folder 'data' there are the images, from the dataset Synapse, already preprocessed and divided by test and train.
In the folder 'model' there are many models used to have a comparison with Swin UNet
and the whole code is in the folder 'TransUNet'

In order to run the train, write in the shell:
```
python train.py --dataset Synapse --cfg configs/swin_tiny_patch4_window7_224_lite.yaml --root_path your DATA_DIR --max_epochs 150 --output_dir your OUT_DIR  --img_size 224 --base_lr 0.05 --batch_size 24
```
Then for train:
```
sh test.sh or python test.py --dataset Synapse --cfg configs/swin_tiny_patch4_window7_224_lite.yaml --is_saveni --volume_path your DATA_DIR --output_dir your OUT_DIR --max_epoch 150 --base_lr 0.05 --img_size 224 --batch_size 24
```
