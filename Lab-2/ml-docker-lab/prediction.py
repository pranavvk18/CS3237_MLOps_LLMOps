import pickle
import numpy as np

# Load the saved model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# Dummy test input
sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])

# Make prediction
prediction = model.predict(sample_input)
print("Predicted class:", prediction[0])
