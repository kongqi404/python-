import tensorflow as tf
import numpy as np
from file_transfer import transfer
from model import Model

x,y=transfer()
print(x.shape)
print(y.shape)