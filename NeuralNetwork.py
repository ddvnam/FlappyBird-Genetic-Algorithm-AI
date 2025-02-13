import numpy as np

class NeuralNetwork:
    def __init__(self, input_node, hidden_nodes, output_nodes):
        self.input_node = input_node 
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = np.random.randn(self.hidden_nodes, self.input_node) # [hidden_nodes, input_node]
        self.bias_h  = np.random.randn(self.hidden_nodes, 1) # [hidden_nodes, 1]

        self.weights_ho = np.random.randn(self.output_nodes, self.hidden_nodes)
        self.bias_o = np.random.randn(self.output_nodes, 1)
        
    def set_weights(self, weights_ih, bias_h, weights_ho, bias_o):
        self.weights_ih = weights_ih
        self.bias_h = bias_h
        self.weights_ho = weights_ho
        self.bias_o = bias_o

    def get_weights(self):
        return self.weights_ih, self.bias_h, self.weights_ho, self.bias_o

    def sigmoid(self,z):
        z = np.clip(z, -500, 500)  # Giới hạn giá trị trong [-500, 500]
        return 1 / (1 + np.exp(-z))

    def relu(self, z):
        return np.maximum(0, z)  

    def feedforward(self, input):
        # input -> hidden
        z1 = np.dot(self.weights_ih, input) + self.bias_h
        a1 = self.relu(z1)  
        # hidden -> output
        z2 = np.dot(self.weights_ho, a1) + self.bias_o
        a2 = self.sigmoid(z2)
        return a2
