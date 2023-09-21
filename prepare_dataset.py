import json
import os
import zipfile
import rarfile
from urllib import request
import cv2
import shutil

def _find_num(jpgpath, dirname, archname, panels):
    fname = os.path.split(jpgpath)[1]
    k = f"{dirname}/{archname}/{fname}"
    if k in panels["second"]:
        return panels["first"][dirname], panels["second"][k]
    return None


def process_img(jpgpath, dirname, archname, outputdir, panels):
    res = _find_num(jpgpath, dirname, archname, panels)
    if res is None:
        return

    img = cv2.imread(jpgpath)
    n1, n2 = res
    n3 = 0
    while True:
        imgk = f"{n1}_{n2}_{n3}.jpg"
        if imgk not in panels["bounding_boxes"]:
            return

        x1, y1, x2, y2 = panels["bounding_boxes"][imgk]

        panel = img[y1:y2, x1:x2]
        cv2.imwrite(os.path.join(outputdir, "bp_"+imgk), panel)
        n3 += 1


if __name__ == "__main__":
    url = "https://light.getcomics.info/Comics%20Marvel/A%20-%20E/Black%20Panther/Black%20Panther%20Vol%201-5%20%281977-2010%29%20GetComics.INFO.zip"

    downloadfile = "tmp.zip"
    tmpdir = "tmp"
    outputdir = "dataset"

    # download
    opener = request.URLopener()
    opener.addheader('User-Agent', 'whatever')
    filename, headers = opener.retrieve(url, downloadfile, reporthook=lambda a,b,c: print(f"{int(a*b/1024**2)} / {int(c/1024**2)} MB downloaded"))

    # load panels
    with open("panels.json", 'r', encoding='utf8') as json_file:
        panels = json.load(json_file)

    os.makedirs(outputdir)

    # extract pages
    with zipfile.ZipFile(downloadfile) as zf:
        cbrs = [f for f in zf.namelist() if f.lower().endswith(".cbr") or f.lower().endswith(".cbz")]
        for cbr in cbrs:
            cbrpath = zf.extract(cbr, path=tmpdir)
            print(cbrpath)
            if zipfile.is_zipfile(cbrpath):
                archfilefunc = zipfile.ZipFile
            elif rarfile.is_rarfile(cbrpath):
                archfilefunc = rarfile.RarFile
            else:
                raise NotImplementedError

            tmp = cbrpath.replace("\\", "/").split("/")
            dirname = tmp[2]
            archname = os.path.splitext(tmp[-1])[0]

            with archfilefunc(cbrpath) as cbrf:
                jpgs = [f for f in cbrf.namelist() if f.lower().endswith(".jpg")]
                for jpg in jpgs:
                    jpgpath = cbrf.extract(jpg, path=tmpdir)

                    process_img(jpgpath, dirname, archname, outputdir, panels)

    print("Dataset ready")
    print("Removing tmp files and folders...")
    os.remove("tmp.zip")
    shutil.rmtree("tmp")
    print("Done!")
