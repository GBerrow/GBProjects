# main.py
import numpy as np
from model import Prediction
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def make_prediction(inputs: list[float], outputs: list[float], input_value: float, plot: bool = False) -> Prediction:
    """
    Make a prediction using linear regression.

    Args:
        inputs (list[float]): List of input values.
        outputs (list[float]): List of output values.
        input_value (float): Input value for prediction.
        plot (bool, optional): Whether to plot the data and the regression line. Defaults to False.

    Returns:
        Prediction: Object containing prediction results.
    """
    # Input validation
    if not all(isinstance(x, (int, float)) for x in inputs):
        raise TypeError("All elements in 'inputs' must be floats or integers.")
    if not all(isinstance(y, (int, float)) for y in outputs):
        raise TypeError("All elements in 'outputs' must be floats or integers.")
    if not isinstance(input_value, (int, float)):
        try:
            input_value = float(input_value)
        except ValueError:
            raise TypeError("'input_value' must be convertible to a float.")

    if len(inputs) != len(outputs):
        raise ValueError('Length of "inputs" and "outputs" must match.')

    # Create a dataframe for our data
    df = pd.DataFrame({'inputs': inputs, 'outputs': outputs})

    # Reshape the data using Numpy (X: Inputs, y: Outputs)
    X = np.array(df['inputs']).reshape(-1, 1)
    y = np.array(df['outputs']).reshape(-1, 1)

    # Split the data into training data to test the model
    train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0, test_size=.20)

    # Initialize the model and test it
    model = LinearRegression()
    model.fit(train_X, train_y)

    # Prediction
    y_prediction = model.predict([[input_value]])
    y_line = model.predict(X)

    # Testing for accuracy
    y_test_prediction = model.predict(test_X)

    # Plotting the data
    if plot:
        display_plot(inputs=X, outputs=y, y_line=y_line)

    # Returning the data
    return Prediction(value=y_prediction[0][0],
                      r2_score=r2_score(test_y, y_test_prediction),
                      slope=model.coef_[0][0],
                      intercept=model.intercept_[0],
                      mean_absolute_error=mean_absolute_error(test_y, y_test_prediction)
                      )

def display_plot(inputs: list[float], outputs: list[float], y_line):
    """
    Display a scatter plot of inputs and outputs with the regression line.

    Args:
        inputs (list[float]): List of input values.
        outputs (list[float]): List of output values.
        y_line: Predicted values.
    """
    plt.scatter(inputs, outputs, s=12)
    plt.xlabel('Inputs')
    plt.ylabel('Outputs')
    plt.plot(inputs, y_line, color='r')
    plt.show()

if __name__ == '__main__':
    # Sample data
    years: list[float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    earnings: list[float] = [1000, 800, 2000, 1500, 3400, 3700, 4000, 3800, 5000, 4800]
    my_input: float = 20

    try:
        # Making the Prediction
        prediction: Prediction = make_prediction(inputs=years, outputs=earnings, input_value=my_input, plot=True)
        print('Input:', my_input)
        print(prediction)
    except Exception as e:
        print("An error occurred:", e)
