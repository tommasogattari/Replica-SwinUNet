Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@tommasogattari 
tommasogattari
/
Progetto-SwinUNet
Public
Cannot fork because you own this repository and are not a member of any organizations.
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Progetto-SwinUNet
/
dataset.md
in
main
 

Spaces

4

Soft wrap
1
# Dataset Synapse
2
Synapse  is a multi-organ segmentation dataset and it is divided into three different folders: training, testing, and labels. The format
3
of these folders is nii.gz that is an open file format commonly used to store brain imaging data obtained using Magnetic Resonance Imaging methods. 
4
In order to unzip files is possibile to use the script 'niigz2png.py' that creates a folder for each of them uploading .png images. 
5
After this, given that the code of processing the data is not available, i wrote 'datapreparation.ipynb' following this guideline:
6
- convert the images to NumPy format
7
- clip the images within [-125, 275]
8
- normalize each 3D image to [0, 1]
9
- for training:
10
    extract 2D slices from 3D volume
11
- while for testing:
12
    keep the 3D volume in h5 format for testing cases 
13
​
14
niigz2png.py guide:
15
copy niigz2png into the folder where the nii.gz files are contained and run from command-line shell:
16
```bash
17
python3 .\niigz2png.py
18
```
19
Then write the input and output folder. For example 
20
```bash
21
Please enter the input folder:
22
training.niigz
23
​
24
```
25
```bash
26
Please enter the output folder:
27
training_synapse
28
```
29
​
30
​
31
If you want to run datapreparation.ipnyb is possibile to use Jupyter Notebook, otherwise they are saved in this github project into these three folers:
32
- training_synapse
33
- testing_synapse
34
- labels
35
​
36
Otherwise, for the official data go to https://drive.google.com/drive/folders/1ACJEoTp-uqfFJ73qS3eUObQh52nGuzCd
37
​
Nessun file selezionato
Attach files by dragging & dropping, selecting or pasting them.
Styling with Markdown is supported
@tommasogattari
Commit changes
Commit summary
Create dataset.md
Optional extended description
Add an optional extended description…
 Commit directly to the main branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.
 
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
