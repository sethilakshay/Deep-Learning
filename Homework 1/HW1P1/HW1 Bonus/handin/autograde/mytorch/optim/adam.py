# Do not import any additional 3rd party external libraries as they will not
# be available to AutoLab and are not needed (or allowed)

import numpy as np

class Adam():
    def __init__(self, model, lr, beta1=0.9, beta2=0.999, eps=1e-8):
        self.l = model.layers
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.lr = lr
        self.t = 0

        self.m_W = [np.zeros(l.W.shape, dtype="f") for l in model.layers]
        self.v_W = [np.zeros(l.W.shape, dtype="f") for l in model.layers]

        self.m_b = [np.zeros(l.b.shape, dtype="f") for l in model.layers]
        self.v_b = [np.zeros(l.b.shape, dtype="f") for l in model.layers]

    def step(self):
        
        self.t += 1
        for layer_id, layer in enumerate(self.l):

            # TODO: Calculate updates for weight
            self.m_W[layer_id] = self.beta1*self.m_W[layer_id] + (1-self.beta1)*layer.dLdW
            self.v_W[layer_id] = self.beta2*self.v_W[layer_id] + (1-self.beta2)*layer.dLdW*layer.dLdW
            
            # TODO: calculate updates for bias
            self.m_b[layer_id] = self.beta1*self.m_b[layer_id] + (1-self.beta1)*layer.dLdb
            self.v_b[layer_id] = self.beta2*self.v_b[layer_id] + (1-self.beta2)*layer.dLdb*layer.dLdb
            
            # TODO: Perform weight and bias updates
            layer.W = layer.W - self.lr*((self.m_W[layer_id]/(1-self.beta1**self.t)) /np.sqrt((self.v_W[layer_id]/(1-self.beta2**self.t)) + self.eps))
            layer.b = layer.b - self.lr*((self.m_b[layer_id]/(1-self.beta1**self.t)) /np.sqrt((self.v_b[layer_id]/(1-self.beta2**self.t)) + self.eps))
