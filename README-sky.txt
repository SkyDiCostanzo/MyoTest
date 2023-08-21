Requirements
- miniconda: https://conda.io/projects/conda/en/latest/user-guide/install/index.html-

conda create --name myotest python=3.8
conda activate myotest
pip install -U myosuite
pip install evalai

git clone https://github.com/SkyDiCostanzo/MyoTest.git
cd path/to/MyoTest
bash setup_no_docker.sh
