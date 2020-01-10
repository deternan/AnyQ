set -e # set -o errexit
set -u # set -o nounset
set -o pipefail 
#in_task_type='train'
#in_task_conf='examples/cnn_pointwise.json'
python3 tf_simnet.py --task 'train' --task_conf 'examples/cnn_pointwise.json'