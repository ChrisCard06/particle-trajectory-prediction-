import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from src.ml.data_generator import generate_orbit_dataset

# Generate dataset
X, Y = generate_orbit_dataset(num_samples=200, steps=500)

# Split into train/test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Define neural network
model = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', max_iter=500)

# Train model
model.fit(X_train, Y_train)

# Evaluate
train_score = model.score(X_train, Y_train)
test_score = model.score(X_test, Y_test)

print(f"Training R^2: {train_score:.3f}")
print(f"Test R^2: {test_score:.3f}")

