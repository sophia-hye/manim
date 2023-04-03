# manim
Manim: an animation engine for precise programmatic animations

## Ready to run
* Install `python`
* Install `FFmpeg` to render `manim`
  * Windows
    1. Download `FFmpeg`: https://ffmpeg.org/download.html#build-windows
    2. Unzip and rename the folder to *ffmpeg*
    3. Move it into the root of *C:/*
    4. Run cmd as an administrator
    5. Set the PATH environment variable for *ffmpeg*: `setx /m PATH "C:/ffmpeg/bin;%PATH%"`
    6. Restart cmd and to check whether `FFmpeg` is installed successfully: `ffmpeg -version`
  * Reference here: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
  * Notice
    * FFmpeg : a cross-platform & open-source software utility to record, convert and stream video/autio files.
    * **NOT** ffmpeg python package
* Install `Tex Live` to run `manim`
  * Linux
    * `sudo apt-get install texlive-latex-extra`
  * Windows
    * Download install file here: https://tug.org/texlive/windows.html
    * **MUST** run `install-tl-windows.exe` as an administrator
      * Notice: it can take long time!

## Install 'Manim'
* Conda
  * ```{python}
    conda create -n my-environment python=3.10
    conda activate my-environment
    conda install -c conda-forge manim
    ```

## Run 'Manim'
* `manim -pql -i <file_name.py> <class_name>`
  * e.g., `manim -pql gradient.py ConvexPlot`