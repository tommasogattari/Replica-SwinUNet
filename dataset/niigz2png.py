
import scipy, shutil, os, nibabel
import sys, getopt
import numpy as np
import imageio


def main(argv, inputf, output):
    inputgz = os.getcwd() + '\\' + inputf
    outputfile = os.getcwd() + '\\' + output
    i=0
    for filename in os.listdir(inputgz):
        i += 1
        inputfile = inputgz + '\\' + filename
        
        try:
            opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
        except getopt.GetoptError:
            print('niigz2png.py -i <inputfile> -o <outputfile>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('niigz2png.py -i <inputfile> -o <outputfile>')
                sys.exit()
            elif opt in ("-i", "--input"):
                inputfile = arg
            elif opt in ("-o", "--output"):
                outputfile = arg

        print('Input file is ', inputfile)
        print('Output folder is ', outputfile)
         # ask if rotate
    

        # set fn as your 4d nifti file
        image_array = nibabel.load(inputfile).get_fdata()
        print(len(image_array.shape))
   
        # else if 3D image inputted
        if len(image_array.shape) == 3:
            # set 4d array dimension values
            nx, ny, nz = image_array.shape

            # set destination folder
            if not os.path.exists(outputfile):
                os.makedirs(outputfile)
                print("Created ouput directory: " + outputfile)

            print('Reading NIfTI file...')

            total_slices = image_array.shape[2]

            slice_counter = 0
            # iterate through slices
            for current_slice in range(0, total_slices):
                # alternate slices
                if (slice_counter % 1) == 0:
                    data = image_array[:, :, current_slice]

                    #alternate slices and save as png
                    if (slice_counter % 1) == 0:
                        print('Saving image...')

                        if inputf == 'averaged-training-labels':
                            image_name = inputfile[:-15] + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
                            data = (data*255).astype('uint8')
                        if inputf == 'averaged-training-images' or inputf == 'averaged-testing-images':
                            image_name = inputfile[:-12] + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
                           
                        imageio.imwrite(image_name, data)
                       
                        print('Saved.')

                        #move images to folder
                        print('Moving image...')
                        src = image_name
                        shutil.move(src, outputfile)
                        slice_counter += 1
                        print('Moved.')

            print(str(i) + 'nii.gz folders to png images')
        
  
    # call the function to start the program
if __name__ == "__main__":
    inputf = input("Please enter the input folder:\n")
    output = input("Please enter the output folder\n")
    main(sys.argv[1:], inputf, output)

