# Python Course for Beginners

These are a series of Jupyter Notebooks that introduce a beginner to the Python programming language. The idea is to let the learner read the explanation, look at a working piece of Python code, modify the code to test one's understanding and progressively learn the language.

The course will cover the following topics:
1. Basic data types
1. Strings
1. Basic input and output via keyboard and screen, including formatted output
1. Lists
1. Tuples
1. Dictionaries
1. Sets
1. Program flow control
1. Boolean expressions
1. Writing functions
1. Modules and packages
1. Python classes and magic dunder functions
1. Miscellaneous topics

## Installing Python - Miniconda3 Python Distribution

Miniconda3 is a minimal Python 3 (Python 3.9 at the time of writing this document) distribution for Windows, MacOSX and Linux. There is also a Python 2 version available but only Python 3 must be used as Python 2 reached end of life in January 2021.

Both 32-bit and 64-bit versions of Miniconda3 are available. Check the operating system and download the correct version. If in doubt, 32-bit version will work on both 32-bit and 64-bit versions whereas 64-bit will work only on 64-bit versions.

Verify the hashes after downloading the installer. The SHA256 hash for each download is displayed in front of the download link.

## Obtaining Miniconda3

URL: https://docs.conda.io/en/latest/miniconda.html

Download the installer for your specific operating system and install. Default options are good enough. The preferred way to install is to install for the current user, create a virtual environment for each project and install only the packages required for that particular project.

To begin using Miniconda Python on Windows, search for **Anaconda Prompt** in **Windows -> Start** and search for **Anaconda Prompt** by typing its name in the search bar and open the Anaconda console.

## First Steps after Installing Miniconda3
Immediately after installing Miniconda3, these are the steps to take in case you wish to use Jupyter Notebooks:
1. Check for any updates to the packages: **`>conda update --all`**
1. Install Jupyter Notebook and its dependencies: **`>conda install notebook`**

## Maintaining the Miniconda3 Installation
Miniconda3 comes with its own package manager named **`conda`**, which also doubles as a virtual environment manager. Using **`conda`**, one can install, update, search and remove packages.

It must be noted that **`conda`** has its own **anaconda repository** of packages and does not install packages from the default Python repository, namely, **PyPI** (https://pypi.org/). There is also an additional repository called **conda-forge** from where some additional packages not in the **anaconda repository** can be installed. But note that not all packages available in PyPI may be available either in the anaconda repository or the conda-forge repository.

To access packages from PyPI, one can use **`pip`** which is installed by default with Miniconda3.

### Using `conda` to maintain packages
**List** all installed packages:

`>conda list`

**List** installed packages with name matching given pattern:

`>conda list num`

will list all installed packages with name matching the pattern **`num`**.

**Search** anaconda repository for a package with name containing the pattern **`num`**":

`>conda search num`

will list all packages in the anaconda repository with name containing the pattern **`num`**:

**Install** a package from anaconda repository:

`>conda install numpy`

will download and install the package named **`numpy`**. If there are other packages that are required for **`numpy`** to work, they too will be downloaded and installed. User must confirm before the download and install process can begin.

**Uninstall** or **remove** an installed package:

`>conda uninstall numpy`

or

`>conda remove numpy`

will remove an installed package named **`numpy`**.

**Update** an installed package:

`>conda update numpy`

will identify if the installed package named **`numpy`** has a newer version available and if available, will download and update the package after confirmation from the user.

**Update** all installed packages:

`>conda update --all`

will check all installed packages for newer versions, and download and install updated versions after user confirmation.

### Using `pip` to maintain packages
PyPI (Python Package Index https://pypi.org) is the main Python repository and **`pip`** is the default package manager.

**List** all installed packages:

`>pip list`

will list all installed packages. Unlike **`conda`**, there is no facility to filter the package names. You can use **`grep`** (use **`find`** on Windows) to filter the output from **`pip`**.

**Search** PyPI for package:

`>pip search numpy`

will search and list all packages in PyPI containing the pattern **`numpy`** in their name. However, note that at the time of writing this document, pip search has been **disabled due to unmanageable load**. See See https://status.python.org/ for more information.

**Install** a package from PyPI:

`>pip install numpy`

will download and install the package **`numpy`** and all its dependencies automatically. It will not wait for user confirmation.

**Uninstall** an installed package:

`>pip uninstall numpy`

will uninstall the installed package **`numpy`** after confirmation from user.

**Update** an installed package or install if not installed:

`>pip install -U numpy`

will check for an update to the installed package named **`numpy`** and if available, will download and update the package. If not installed, it will be downloaded and installed.

There is no facility in **`pip`** to update all packages that have newer versions. However, there is a facility to list the packages that have a newer version:

`'pip list -o`

will display the list of installed packages whose newer versions are available.

**NOTE:**
1. PyPI is the superset of all Python packages and has all packages that are available in **anaconda** and **conda-forge** repositories.
1. Most recent version of packages are first available in PyPI. The same package may be slightly delayed to appear in anaconda and conda-forge as they are downstream repositories.
1. It is best to install a package from anaconda or conda-forge, and install from PyPI only when the required package is not available in either of them.
1. As far as possible, update packages installed from PyPI using **`pip`** and packages installed from anaconda or conda-forge using **`conda`**. Avoid mixing the repositories.

## Virtual Environments
Virtual environments allow the programmer to create isolated environment, with its own version of packages specific to a project. This allows a developer to simultaneously work on different projects with different versions of packages specific to each project.

In addition, **`conda`** allows installation a specific version of Python for each project.

### Using `conda` to manage virtual environments

On Windows, the default environment is named **`base`** and that is the one activated when you open **Anaconda Prompt**. User defined virtual environments can be created from the **`base`** environment or any other previously created user defined virtual envirom=nment.

The name of the current environment is indicated at the start of the prompt, within parentheses. For example, **`(base)`** indicates that the current environment is **`base`**.

**Create** a virtual environment

`>conda create -n py39`

will create a new virtual environment named **`py39`**. It will contain the version of Python currently installed on your machine and will be populated with **`conda`**, **`pip`** and a few other essential packages.

**Activate** a virtual environment: Once a virtual environment has been created, it must be activated. The first task after activating a virtual environment is to update the package managers **`conda`** and **`pip`** and install any other required packages.

`>conda activate py39`

will activate the virtual environment named **`py39`**. The command prompt will display **`(py39)`** to the left to indicate the current virtual environment that is active.

**Deactivate** a virtual environment:

`>conda deactivate`

will deactivate the active virtual environment if it is not the default environment **`base`**.
