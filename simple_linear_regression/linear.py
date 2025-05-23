import jax
import jax.numpy as jnp

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = jnp.array([])
        self.bias = 0
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = jnp.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            y_pred = jnp.dot(X, self.weights) + self.bias

            dw = (1/n_samples) * jnp.dot(X.T, (y_pred-y))
            db = (1/n_samples) * jnp.sum(y_pred-y)

            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db

    def predict(self, X):
        y_pred = jnp.dot(X, self.weights) + self.bias
        return y_pred
        


        
        


