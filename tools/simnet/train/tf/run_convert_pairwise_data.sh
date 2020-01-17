set -e # set -o errexit
set -u # set -o nounset
set -o pipefail 
echo "convert train data"
python ./tools/tf_record_writer.py pairwise ./data/train_.tsv ./data/convert_train_pairwise 0 32
echo "convert test data"
python ./tools/tf_record_writer.py pairwise ./data/test_.tsv ./data/convert_test_pairwise 0 32
echo "convert data finish"