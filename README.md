*README.md is still under construction*

## About
This Python project reconstructs faces from image datasets using Linear Algebra concepts. To reconstruct the face, the mean facial image of the dataset is computed (a dataset of 400 images), and then the eigenfaces are scaled by the weights and added to the mean facial image.

In addition to adding the Jupyter Notebook, I have also included the Python file. Using the Jupyter Notebook, you can view the results and reasoning behind code implementations very quickly.

## Compile Instructions
This program was developed using Ubuntu using Jupyter Notebook, but I will include compile instructions for Windows as well.

### Windows
 * Install all necessary libraies if you do not have them already, for me this list included:
   * C:\Python310\python.exe -m pip install --upgrade pip --user
     * The path at the start of this command will likely change for you, the terminal may tell you what to enter
   * python -m pip install -U matplotlib --user
   * python -m pip install -U pip --user
 * Then while the terminal is in the directory containing the notebook file and folder, enter the command "python -m notebook"
 * Once the homepage is loaded, select the file named "reconstruct.ipynb"
 * Once you are on this page, click Run on the toolbar to run the program cell by cell.
