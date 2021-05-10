# GW Open Data Workshop #4
May 10 - 14, 2021
<p align="middle">
  <img src="https://indico.in2p3.fr/event/18313/logo-786578160.png" width="150" />
  &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp;
</p>

This repository contains the material to support [GW Open Data Workshop #4](https://www.gw-openscience.org/static/workshop4/).

Firstly, we recommend taking a look at the <a href="setup/setup.md">setup guide</a>, where you can find the information to configure the workspace where you are going to execute the tutorials.

In the [Tutorials](./Tutorials/) folder, you can find the various notebooks for the three days, divided on the base of their topics. There are also some quiz that you are asked to complete at the end of each session.

<<<<<<< HEAD
Lastly, test yourself with the [GW Data Challenge](./Challenge/)!
=======
Lastly, test yourself with the [GW Data Challenge](./Challenge/)!

## Software setup on Linux

</a>

<img src='https://www.wispresort.com/uploadedImages/Winter/intermediate.png' width=20 /> Intermediate (Some software installation; Will not work on Windows PC)

<img src='./share/video-icon.png' width=18 /> [Video instructions](https://drive.google.com/file/d/1YZcaY-35JiHXOH4unRe5ECSeDl8IZFZy/view?usp=sharing)

This workshop uses [Python version 3.8](https://www.python.org/downloads/release/python-380/). We recommend creating a [Python virtual environment](https://docs.python.org/3.8/tutorial/venv.html) and install all the package dependencies there. The official environment with all the required packages is [igwn-py38](https://computing.docs.ligo.org/conda/environments/igwn-py38/), available from the International Gravitational-Wave Observatory Network ([IGWN](https://computing.docs.ligo.org/guide/)) community website. However, we make available also a *light-weight* version of this environment, with only the strictly necessary packages to execute the notebooks. Whenever possible, we recommend the full installation though

This guide will walk you through the configuration of this environment with [Conda](https://www.anaconda.com/). 

1. Install miniconda:
   
    - Visit the website https://conda.io/en/latest/miniconda.html
    - Choose the version for Python 3.8
    - Follow the [installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/
) for your operating system: 
        - [Linux](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)
        - [macOS](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)
    
   You may need to restart your computer after installation.

2. If you want to install the full [igwn-py38 environment](https://computing.docs.ligo.org/conda/environments/igwn-py38/) (recommended), download the YML dependencies file for the IGWN website:
   * [YML file for Linux](https://computing.docs.ligo.org/conda/environments/linux/igwn-py38.yaml)
   * [YAML file for macOS](https://computing.docs.ligo.org/conda/environments/osx/igwn-py38.yaml)

   Instead, for the *light-weight* environment, download the YML file corresponding to your operating system from this repository:
   * [YAML file for linux](./environment.yml)
   * [YAML file for macOS](./igwn-py38-lw-macOS.yaml)

   **Note:** the name of the *light-weight* environment is **igwn-py38-lw** to distinguish it from the official one, `igwn-py38`. In the following steps, remember to add the "`-lw`" subfix to the name.

3. Add the conda-forge channel

    `conda config --add channels conda-forge`

4. Create the environment. <br/>
   If you have downloaded the full environment, either on Linux or macOS:
   
   `conda env create --file igwn-py38.yaml`
   
   Otherwise, for the light-weight one: <br/>
   * On Linux: `conda env create --file environment.yml`
   * On macOS: `conda env create --file igwn-py38-lw-macOS.yaml`

5. Clone the workshop git repo 

    `git clone https://github.com/gw-odw/odw-2021.git`

6. Move into the directory with the workshop git repo 

    `cd odw-2021`
    
7. Activate the environment. <br/>
   **Note:** remember to add "`-lw`" to the name of the environment if you have installed the light-weight one.

   `conda activate igwn-py38`
   
   (Light-weight environment: `conda activate igwn-py38-lw`)

8. Build a custom [jupyter kernel](https://ipython.readthedocs.io/en/stable/install/kernel_install.html) using the command 

  `ipython kernel install --user --name=igwn-py38` 
  
  or equivalently 
  
  `python -m ipykernel install --user --name=igwn-py38`
  
  (Light-weight environment: `--name=igwn-py38-lw`)

9. Start the Jupyter notebook server <br/>
  `jupyter notebook` and select the kernel `igwn-py38` (`igwn-py38-lw`) if this is not done by default.

**Notebooks:**
If you are not familiar with Jupyter notebooks, google one of the many introductory guides available on the internat, like <a href="https://realpython.com/jupyter-notebook-introduction/">this one</a>. Also, taking a look at the <a href="https://colab.research.google.com/notebooks/basic_features_overview.ipynb">Examples</a> offered by Google Colab can be helpful.

**Troubleshooting:**
- The kernel `igwn-py38` should appear in the list returned by the command `jupyter kernelspec list` executed in a terminal
- If, when you run jupyter, you get the message: `Could not find kernel matching igwn-py38. Please select a kernel: Python 3`
this indicates the `igwn-py38` kernel is not installed properly. Make sure you executed step 9)
- Having the full environment and the light-weight one with two different names allows them to coexist. If you want to leave the same name and overwrtite one or the other, simply add `--force` option when you create it.
>>>>>>> ef7d5d6a278447f98b9d28e9ffc7fc452d284c72
