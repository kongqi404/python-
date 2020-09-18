import tensorflow as tf


def Model():
    models = tf.keras.Sequential(name="srcnn")
    models.add(tf.keras.layers.Conv2D(64, 9, padding='SAME', activation=tf.keras.activations.relu,
                                      input_shape=(1920, 1080, 3,)))
    models.add(tf.keras.layers.Conv2D(32, 3, padding='SAME', activation=tf.keras.activations.relu))
    """
  1*1卷积为可选
    """
    models.add(tf.keras.layers.Conv2D(32, 1, activation=tf.keras.activations.relu))
    models.add(tf.keras.layers.Conv2D(3, 5, padding='SAME'))
    models.compile(optimizer='adam', loss=tf.keras.losses.MSE, metrics=["accuracy"])
    return models
