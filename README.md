# COMICORDA: A Novel Dataset for Dialogue Act Recognition in Comics

This repository contains COMICORDA dataset in JSON file.

This dataset is an extension of the EMORECOM dataset [https://github.com/aisutd/emorecom]() that was used in ICDAR2021 Competition **Multimodal Emotion Recognition on Comics scenes**
 [https://sites.google.com/view/emotion-recognition-for-comics]()


The original source of images: [https://obj.umiacs.umd.edu/comics/index.html]()

[Download images](https://obj.umiacs.umd.edu/comics/raw_panel_images.tar.gz)

JSON file with annotated Dialogue Acts: `data.json`. To filter out panels that contain at least one speech balloon use `"error_code": 0`. All possible values of this `error_code` item are as follows:
 - `"error_code": 0` ==> at least one speech balloon
 - `"error_code": 1` ==> neither dialog nor narration (just an image without text)
 - `"error_code": 2` ==> Narration balloon present, but no dialog (no speech balloons)

See example: `example.ipynb`

To be able to replicate the experiments, do as follows:

1. Download the first part of the COMICORDA dataset. The source of images is either the subset from the EMORECOM website or the whole collection of 1.2 million extracted panels from the original source of images above. If you have downloaded panels from [https://obj.umiacs.umd.edu/comics/index.html](), the first number in `img_id` is the folder name (e.g. `"img_id": "938_3_4"` means folder `938` and filename `3_4.jpg` within.)

```
raw_panel_images
|--- 0
     |---0_0.jpg
     |---0_1.jpg
      ...
     |---
|--- 1
     |---0_0.jpg
     |---0_1.jpg
      ...
     |---
|--- 2
     |---0_0.jpg
     |---0_1.jpg
      ...
     |---
....
|--- 3958
     |---0_0.jpg
     |---0_1.jpg
      ...
     |---
```

2. Run script `prepare_dataset.py` that downloads the second part of the dataset (panels with filename mask bp_<img_id>).
3. Load `data.json` and check whether all 1438 images are available. We recommend to merge all 1438 images/panels into one folder.
4. Run desired experiments.
