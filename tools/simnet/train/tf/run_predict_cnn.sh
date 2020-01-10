set -e # set -o errexit
set -u # set -o nounset
set -o pipefail 
#in_task_type='predict'
#in_task_conf='./examples/cnn-pointwise.json'
python3 tf_simnet.py --task 'predict' --task_conf 'examples/cnn_pointwise.json'