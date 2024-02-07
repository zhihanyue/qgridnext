# Test environments

To test QgridNext in different environments, several conda environments (*.yml) are presented in this directory. It can be tested as follows:

```sh
cd /path/to/repo
conda env create -f test_envs/xxx.yml
conda activate qgridnext-xxx
pip install .   # install QgridNext
pytest   # test basic functions

# To test QgridNext's compatibility, run jupyter and check example.ipynb manually in your browser:
bash test_envs/launch_lab.sh   # run jupyter lab
bash test_envs/launch_notebook.sh  # run jupyter notebook
bash test_envs/launch_voila.sh  # run voila
```
