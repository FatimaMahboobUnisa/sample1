import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

class ReinforcementLearningAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.model = self._build_model()

    def _build_model(self):
        """Define the RL model architecture."""
        model = Sequential([
            Dense(24, activation='relu', input_dim=self.state_size),
            Dense(24, activation='relu'),
            Dense(self.action_size, activation='linear')
        ])
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=0.001))
        return model

    def predict_action(self, state):
        """Predict optimal action for a given network state."""
        return np.argmax(self.model.predict(state))

# Example Usage
if __name__ == "__main__":
    state_size = 10  # Input features (e.g., latency, bandwidth, packet loss)
    action_size = 5  # Possible actions (e.g., reroute traffic, adjust QoS)
    
    agent = ReinforcementLearningAgent(state_size, action_size)
    sample_state = np.random.rand(1, state_size)
    action = agent.predict_action(sample_state)
    print(f"Predicted optimal action: {action}")
