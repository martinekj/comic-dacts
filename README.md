# COMICORDA: A Novel Dataset for Dialogue Act Recognition in Comics

This repository contains COMICORDA dataset in JSON file.

This dataset is an extension of the EMORECOM dataset [https://github.com/aisutd/emorecom]() that was used in ICDAR2021 Competition **Multimodal Emotion Recognition on Comics scenes**
 [https://sites.google.com/view/emotion-recognition-for-comics]()


The original source of images: [https://obj.umiacs.umd.edu/comics/index.html]()

[Download images](https://obj.umiacs.umd.edu/comics/raw_panel_images.tar.gz)

JSON file with annotated Dialogue Acts: `data.json`

See example: `example.ipynb`

To be able to replicate the experiments, do as follows:

1. Download the first dataset. The source of images is either the subset from the EMORECOM website or the whole collection of 1.2 million extracted panels from the original source of images above.
2. Run script `prepare_dataset.py` that downloads the second dataset.
3. Merge all images of extracted panels into a single folder
4. Load `data.json` file and check if all 1438 images are available.
5. Run desired experiments
