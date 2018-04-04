# Based on https://www.thoughtvector.io/blog/deployment-with-anaconda/

sudo yum install git
curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh
sh miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
git clone https://github.com/empirical-org/Quill-NLP-API.git
cd Quill-NLP-API/
conda create -n app spacy Flask gunicorn tensorflow nltk python=3
source activate app
pip install tflearn
python -m spacy download en_core_web_lg
QUILL_SPACY_MODEL=en_core_web_lg FLASK_APP=app.py flask run # and boom goes the dynamite