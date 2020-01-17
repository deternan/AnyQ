set -e # set -o errexit
set -u # set -o nounset
set -o pipefail 
echo "convert train data"
python ./tools/tf_record_writer.py pointwise ./data/train_.tsv ./data/convert_train_ 0 32
echo "convert test data"
python ./tools/tf_record_writer.py pointwise ./data/test_.tsv ./data/convert_test_ 0 32
echo "convert data finish"