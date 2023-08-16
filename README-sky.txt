conda create --name MyoSuite python=3.8
conda activate myotest
pip install -U myosuite

git clone https://github.com/SkyDiCostanzo/MyoTest.git
pip install evalai
bash setup_no_docker.sh
