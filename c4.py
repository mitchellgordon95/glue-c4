import tensorflow as tf
import tensorflow_datasets as tfds

tfds.text.c4.C4(data_dir='/exp/mgordon/glue-c4/data', config='en.noclean').download_and_prepare()
