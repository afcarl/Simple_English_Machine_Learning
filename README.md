# Simple_English_Machine_Learning
Simple, easy to read implementations of common Machine Learning algorithms. 

Wikipedia's Simple English language option makes articles available to children and adults learning English. While 
performant, distributed implementations of Machine Learning algorithms are a practitioner's toolset, I've found 
myself coding up simple implementations algorithms to better understand them.  

With these goals in mind, I've created this repo, with simple, straight forward implementations. These 
implementations should be easy to read and understand, and give the intuition of the algorithm without supporting 
prose. 
  
## Getting started

### Repo structure
Where important things are. 

### Python Environment
Python code in this repo utilizes packages that are not part of the common library. To make sure you have all of the 
appropriate packages, please install [Anaconda](https://www.continuum.io/downloads), and install the environment 
described in environment.yml (Instructions [here](http://conda.pydata.org/docs/using/envs.html), under *Use 
environment from file*, and *Change environments (activate/deactivate)*). 

### To run code
  
To run the Python code, complete the following:
```bash
# Install anaconda environment
conda env create -f environment.yml 
# Make a note of the environment name (e.g. source activate environment_name)

# Activate environment
source activate simple

# Run script. Note that scripts must be run from the highest folder in the repo
python bin/file_name.py

# Revert to previous Python distribution
source deactivate
```

## Design Choices
TODO
 - SKLearn interface
 - Package choices
 - Based on ISL / ESL

## Contact
Feel free to contact me at 13herger <at> gmail <dot> com

