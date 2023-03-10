# SwinUNet-Project
This study presents a paper that concerns the utilization and the potential of Swin Transformer-based to be applied in the vision domain, in particular in the medical domain comparing the results with the various convolutional neural network (CNN). The proposed method is a novel approach known as Swin-Unet, which is a pure Transformer-based U-shaped Encoder-Decoder architecture for medical image segmentation. The method incorporates skip-connections and employs a hierarchical Swin Transformer with shifted windows as the encoder and a symmetric Swin Transformer-based decoder with a patch expanding layer for up-sampling. Experimental evaluations on multi-organ datasets that the proposed method outperforms existing methods that utilize full convolution or a combination of transformer and convolution. The codes and trained models used in this study are publicly available on GitHub https://github.com/HuCaoFighting/Swin-Unet.

The GitHub repository structure is composed by:

- [dataset](https://github.com/tommasogattari/Progetto-SwinUNet/tree/main/dataset) is the folder that contains the guide for the dataset Synapse used by the author of the paper
- [UNet](https://github.com/tommasogattari/Progetto-SwinUNet/blob/main/UNet.ipynb) 
- [Swin UNet unofficial](https://github.com/tommasogattari/Progetto-SwinUNet/blob/main/Swin%20Unet%20unofficial.ipynb) 
- [Swin UNet official replicated](https://github.com/tommasogattari/Replica-SwinUNet/blob/main/Swin%20UNet%20replica.md)

In the histogram below there are the results of differents UNet-based architecture ordered by each mean dice value

![Main Results.png](https://github.com/tommasogattari/Progetto-SwinUNet/blob/main/Main%20Results.png)

# References

- [TransUNet](https://github.com/Beckschen/TransUNet)
- [SwinTransformer](https://github.com/microsoft/Swin-Transformer)
