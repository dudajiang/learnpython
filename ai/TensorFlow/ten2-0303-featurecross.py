import math

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

df = pd.read_csv("0301.csv", sep=",")
df.rename(columns={'Unnamed: 0': 'rand'}, inplace=True)
df = df.reindex(np.random.permutation(df.index))
print(df.describe())


# 对数据集进行预处理
def preprocess_features(dataframe):
    """对数据集中的特征部分进行预处理.
    所有的预处理都可以在这里进行，包括独热编码，分箱，特征组合等都可以

    Args:
      dataframe: A Pandas DataFrame expected to contain data
    Returns:
      A DataFrame that contains the features to be used for the model, including
      synthetic features.
    """
    selected_features = dataframe[
        ["trainx", "rand"]]
    processed_features = selected_features.copy()
    # Create a synthetic feature.
    # processed_features["rooms_per_person"] = (
    #   dataframe["total_rooms"] /
    #   dataframe["population"])
    return processed_features


def preprocess_targets(dataframe):
    """对数据集的标签部分做处理.

    Args:
      dataframe: A Pandas DataFrame expected to contain data
    Returns:
      A DataFrame that contains the target feature.
    """
    output_targets = pd.DataFrame()
    # Scale the target to be in units of thousands of dollars.
    output_targets["trainy"] = (
        dataframe["trainy"] / 10000.0)
    return output_targets


# 一、定义输入函数
def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """用一个特征训练线性模型

    参数:
      features: pandas DataFrame of features
      targets: pandas DataFrame of targets
      batch_size: Size of batches to be passed to the model
      shuffle: True or False. Whether to shuffle the data.
      num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
    Returns:
      Tuple of (features, labels) for next data batch
    """

    # Convert pandas data into a dict of np arrays.
    features = {key: np.array(value) for key, value in dict(features).items()}

    # Construct a dataset, and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features, targets))  # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)

    # Shuffle the data, if specified.
    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    # Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels

# 定义特征列


def construct_feature_columns(input_features):
    """构建多个特征.

    Args:
      input_features: The names of the numerical input features to use.
    Returns:
      A set of feature columns
    """
    return set([tf.feature_column.numeric_column(my_feature)
                for my_feature in input_features])

# 二、训练模型


def train_model(learning_rate, steps, batch_size,
                training_examples,
                training_targets,
                validation_examples,
                validation_targets):
    """Trains a linear regression model of multiple feature.

    Args:
      learning_rate: A `float`, the learning rate.
      steps: A non-zero `int`, the total number of training steps. A training step
        consists of a forward and backward pass using a single batch.
      batch_size: A non-zero `int`, the batch size.
      后面四个参数分别是训练集和特征和标签，以及验证集的特征和标签
    """

    periods = 10
    steps_per_period = steps / periods

    my_feature = "trainx"
    my_label = "trainy"

    # 定义线性回归的优化器和模型等.
    my_optimizer = tf.train.GradientDescentOptimizer(
        learning_rate=learning_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(
        my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns=construct_feature_columns(training_examples),
        optimizer=my_optimizer
    )

    # 定义输入函数.
    def training_input_fn(): return my_input_fn(
        training_examples,
        training_targets[my_label],
        batch_size=batch_size)

    def predict_training_input_fn(): return my_input_fn(
        training_examples,
        training_targets[my_label],
        num_epochs=1,
        shuffle=False)

    def predict_validation_input_fn(): return my_input_fn(
        validation_examples, validation_targets[my_label],
        num_epochs=1,
        shuffle=False)

    # 画图.
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    plt.title("Learned Line by Period")
    plt.ylabel(my_label)
    plt.xlabel(my_feature)
    sample = df.sample(n=20)
    plt.scatter(sample[my_feature], sample[my_label])
    colors = [cm.coolwarm(x) for x in np.linspace(-1, 1, periods)]

    # Train the model, but do so inside a loop so that we can periodically assess
    # loss metrics.
    print("Training model...")
    print("RMSE (on training data):")
    training_rmse = []
    validation_rmse = []
    for period in range(0, periods):
        # Train the model, starting from the prior state.
        linear_regressor.train(
            input_fn=training_input_fn,
            steps=steps_per_period
        )
        # Take a break and compute predictions.
        training_predictions = linear_regressor.predict(
            input_fn=predict_training_input_fn)
        training_predictions = np.array(
            [item['predictions'][0] for item in training_predictions])

        validation_predictions = linear_regressor.predict(
            input_fn=predict_validation_input_fn)
        validation_predictions = np.array(
            [item['predictions'][0] for item in validation_predictions])

        # Compute loss.
        training_root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(training_predictions, training_targets))
        validation_root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(validation_predictions, validation_targets))
        # Occasionally print the current loss.
        print("  period %02d : %0.2f" %
              (period, training_root_mean_squared_error))
        # Add the loss metrics from this period to our list.
        training_rmse.append(training_root_mean_squared_error)
        validation_rmse.append(validation_root_mean_squared_error)
        # Finally, track the weights and biases over time.
        # Apply some math to ensure that the data and line are plotted neatly.
        # y_extents = np.array([0, sample[my_label].max()])

        # weight = linear_regressor.get_variable_value(
        #     'linear/linear_model/%s/weights' % input_feature)[0]
        # bias = linear_regressor.get_variable_value(
        #     'linear/linear_model/bias_weights')

        # x_extents = (y_extents - bias) / weight
        # x_extents = np.maximum(np.minimum(x_extents,
        #                                   sample[my_feature].max()),
        #                        sample[my_feature].min())
        # y_extents = weight * x_extents + bias
        # plt.plot(x_extents, y_extents, color=colors[period])
    print("Model training finished.")

    # Output a graph of loss metrics over periods.
    plt.subplot(1, 2, 2)
    plt.ylabel('RMSE')
    plt.xlabel('Periods')
    plt.title("Root Mean Squared Error vs. Periods")
    plt.tight_layout()
    plt.plot(training_rmse, label="training")
    plt.plot(validation_rmse, label="validation")
    plt.legend()

    # Output a table with calibration data.
    calibration_data = pd.DataFrame()
    calibration_data["training_predictions"] = pd.Series(training_predictions)
    calibration_data["validation_predictions"] = pd.Series(
        validation_predictions)
    calibration_data["training_targets"] = pd.Series(training_targets[my_label)
    calibration_data["validation_targets"] = pd.Series(validation_targets[my_label)
    display.display(calibration_data.describe())

    print("Final RMSE (on training data): %0.2f" %
          training_root_mean_squared_error)

    return linear_regressor

if __name__ == "__main__":
    training_examples = preprocess_features(df.head(1500))
    print(training_examples.describe())
    training_targets = preprocess_targets(df.head(1500))
    training_targets.describe()
    validation_examples = preprocess_features(df.tail(500))
    validation_examples.describe()
    validation_targets = preprocess_targets(df.tail(500))
    validation_targets.describe()

    minimal_features= [
      "trainx"
    ]

    minimal_training_examples= training_examples[minimal_features]
    minimal_validation_examples= validation_examples[minimal_features]

    linear_regressor = train_model(
        learning_rate=0.00003,
        steps=500,
        batch_size=5,
        training_examples=minimal_training_examples,
        training_targets=training_targets,
        validation_examples=minimal_validation_examples,
        validation_targets=validation_targets)


    test_data = pd.read_csv("0302.csv", sep=",")
    test_data.rename(columns={'Unnamed: 0': 'rand'}, inplace=True)
    test_examples = preprocess_features(test_data)
    test_targets = preprocess_targets(test_data)

    predict_test_input_fn = lambda: my_input_fn(
          test_examples,
          test_targets["trainy"],
          num_epochs=1,
          shuffle=False)

    test_predictions=linear_regressor.predict(input_fn=predict_test_input_fn)
    test_predictions=np.array([item['predictions'][0]
                              for item in test_predictions])

    root_mean_squared_error=math.sqrt(
        metrics.mean_squared_error(test_predictions, test_targets))

    print("Final RMSE (on test data): %0.2f" % root_mean_squared_error)