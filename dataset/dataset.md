
# Dataset Synapse
Synapse  is a multi-organ segmentation dataset and it is divided into three different folders: training, testing, and labels. The format
of these folders is nii.gz that is an open file format commonly used to store brain imaging data obtained using Magnetic Resonance Imaging methods. In order to unzip files is possibile to use the script 'niigz2png.py' that creates a folder for each of them uploading .png images. After this, given that the code of processing the data is not available from the original code, i wrote 'datapreparation.ipynb' following this guideline:
- convert the images to NumPy format
- clip the images within [-125, 275]
- normalize each 3D image to [0, 1]
- for training:
- extract 2D slices from 3D volume
- while for testing:
   - keep the 3D volume in h5 format for testing cases 

niigz2png.py guide:
copy niigz2png into the folder where the nii.gz files are contained and run from command-line shell:

```bash
python3 .\niigz2png.py
```
Then write the input and output folder. For example: 
```bash
Please enter the input folder:
training.niigz
```
```bash
Please enter the output folder:
training_synapse
```
If you want to run datapreparation.ipnyb is possibile to use Jupyter Notebook, otherwise they are saved in this github project into these three folers:

- training_synapse
- testing_synapse
- labels

Otherwise, for the official data already preprocessed go to https://drive.google.com/drive/folders/1ACJEoTp-uqfFJ73qS3eUObQh52nGuzCd
