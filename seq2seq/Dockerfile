# use ubuntu as base image
FROM ubuntu

# run updates, install python3 and tensorflow
RUN apt-get update && apt-get install -y \
locales \
python3 \
python-pip \
python-tk \
git \
nano \
vim \
wget

# set locale 
RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

# make course directories
RUN mkdir tools


# install tensorflow via pip 
RUN pip install tensorflow==1.4.1

# install google seq2seq and char-rnn-tensorflow
RUN git clone https://github.com/google/seq2seq.git /tools/seq2seq
RUN git clone https://github.com/sherjilozair/char-rnn-tensorflow /tools/charnn

# install dependencies
WORKDIR tools/seq2seq
RUN pip install -e . 

RUN sed -i 's/from tensorflow.contrib.distributions.python.ops import bernoulli/from tensorflow.contrib.distributions import Bernoulli/' /tools/seq2seq/seq2seq/contrib/seq2seq/helper.py
RUN sed -i 's/from tensorflow.contrib.distributions.python.ops import categorical/from tensorflow.contrib.distributions import Categorical/' /tools/seq2seq/seq2seq/contrib/seq2seq/helper.py
