# Python for Earth Sciences

Instructor: [Rebekah Esmaili](http://www.rebekahesmaili.com), PhD

---

A crash course in Python focusing on reading and visualizing data sets used in the Earth sciences.

This code is interactive! Click here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/modern-tools-workshop/ESSIC-workshop-2023/HEAD)

---

## Getting Started

This workshop will cover:

* Launching Jupyter Notebooks
* Working with arrays using the Numpy package
* Importing text datasets using the Pandas package
* Creating simple graphics with Matplotlib
* Importing scientific data formats, such as netCDF and HDF5
* Creating maps from datasets

---

### Installation Requirements

"I am  new to Python and just want to learn!"

* I recommend launching Binder, an online service that shares a "cloud version" of this course. No installation required! [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/modern-tools-workshop/ESSIC-workshop-2023/HEAD)
    * Need help with Binder? Video tutorial on [YouTube](https://youtu.be/3BrfFe4HsAw).
* Best option if you are a Python tourist!

With Binder, everything is pre-installed and will open in JupyterLab. No installation or login required! There are some limitations to using Binder:

* Startup can take anywhere from 30 seconds to 30 minutes, depending on when it was last built
* Sessions expire with 10 minutes of inactivity
* Data does not persist between sessions (this is for learning only, you'll have to install python locally to code on your own)
* Limited to 100 simultaneous users per session

"I want to start using Python in my research!"

* If you wish to run the examples locally, I recommend installing [Anaconda](https://www.anaconda.com/products/individual). If you are having trouble with your installation, contact the instructor before the course or use Binder.
    * Need help installing Anaconda? Video tutorial on [YouTube](https://youtu.be/zxSQCXXvOIM).
* Download the contents of this GitHub repository to your computer.
* Launch Jupyter Notebooks from the Anaconda Navigator. This will open a window in your default browser. Navigate to the folder that contains the notebooks (*.ipynb) and click on the tutorial for the day.
    * New to Jupyter? Here's a video tutorial on [YouTube](https://youtu.be/gmMCuR9JPpY).
* Additional packages:
  * Launch the Anaconda Prompt (Windows) or Terminal (MacOS/Linux).
  * Use the environments.yml to install the necessary packages. You can do this in the terminal using:

    ```bash
    conda env create -f environment.yml
    ```

  * Then, switch to the new environment once the installation is complete:

    ```bash
    conda activate python-workshop
    ```
  * Note: The default environment is called 'base.' If you close the terminal, you will have to switch back to the environment using the above command again.

I *do not* recommend using the following: 
* Python on a remote server for this tutorial
* Your operating system Python
* Shared Python installations


Given that participants have a lot of different operating systems and versions of Python, it's best if we're all using the same tools. If you *really* want to do one of the above, I recommend making a new environment using the environment.yml file.


---
## Course Philosophy

* Increase accessibility of satellite data and analysis
* Teach Python using practical examples and real-world datasets
* Promote reproducible and transparent scientific research

## Resources

### Packages and Tutorials

Pandas
* Short Introduction: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
* Cookbook for more details: https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#cookbook

---
 Matplotlib
* Pyplot Tutorial: https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html

---
Import/Export

NetCDF files
* Detailed tutorial on the netCDF4 package: https://unidata.github.io/netcdf4-python.
* Xarray tutorial: https://xarray-contrib.github.io/xarray-tutorial/

HDF files
* The package [h5py](https://www.h5py.org/) is similar to netcdf4.
* User manual at http://docs.h5py.org/en/stable/.
* Xarray can also open HDF files!

GRIB/GRIB2 files
* World Meteorology Association standard format, e.g. commonly used with weather-related models like ECMWF and GFS.
* Can be opened using [pygrib](https://github.com/jswhit/pygrib).
* Example usage at https://jswhit.github.io/pygrib/docs/.

BUFR files
* Another common table-driven format.
* Open with [python-bufr](https://github.com/pytroll/python-bufr), part of the pytroll project.
---    

### General Python Resources   

Beginner Tutorials
* Youtube series for absolute beginners [CS Dojo](https://www.youtube.com/watch?v=Z1Yd7upQsXY&list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg)
* [Research Software Engineering with Python](https://merely-useful.tech/py-rse/) Free eBook to enhance your workflow.

Intermediate Tutorials
* [Project Pythia Foundations Online Textbook](https://foundations.projectpythia.org/landing-page.html) A community learning resource for Python-based computing in the geosciences. Highly recommended!
* [Python for Climate and Meteorology](https://www.youtube.com/watch?v=uQZAEPnUZ5o) Another tutorial taught at AMS, a little more advanced.
* Learn more about [Python for Atmosphere and Ocean Scientists](https://carpentries-lab.github.io/python-aos-lesson/) using Software Carpentry lesson plans.
* [Earth Observation using Python](https://www.wiley.com/en-us/Earth+Observation+using+Python%3A+A+Practical+Programming+Guide-p-9781119606888) is a book I wrote that builds on the content of the workshop.

## Granting Permission for Reuse
These course materials are the intellectual property of the instructor. However, I encourage others to reuse or adapt the material for their research communities or use cases. If you do not significantly modify the original material, please send me an email letting me know and acknowledge me in your content.