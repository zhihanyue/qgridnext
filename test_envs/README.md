# Test environments

To facilitate testing QgridNext across various environments, this directory includes several conda environment files (*.yml). You can test QgridNext in these environments by following the steps below:

```sh
git clone https://github.com/zhihanyue/qgridnext
cd qgridnext
conda env create -f test_envs/xxx.yml
conda activate qgridnext-xxx
pytest   # test basic functions

# To test QgridNext's compatibility, run jupyter and check example.ipynb manually in your browser:
bash test_envs/launch_lab.sh   # run jupyter lab
bash test_envs/launch_notebook.sh  # run jupyter notebook
bash test_envs/launch_voila.sh  # run voila
```
