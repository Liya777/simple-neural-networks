import numpy as np
import neuralnets as nn
import matplotlib.pyplot as plt

np.random.seed(1)
x = np.linspace(-1, 1, 200)[:, None]       # [batch, 1]
y = x ** 2                                  # [batch, 1]

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        w_init = nn.init.RandomUniform()
        b_init = nn.init.Constant(0.1)

        self.l1 = nn.layers.Dense(1, 10, nn.act.tanh, w_init, b_init)
        self.l2 = nn.layers.Dense(10, 10, nn.act.tanh, w_init, b_init)
        self.out = nn.layers.Dense(10, 1, w_initializer=w_init, b_initializer=b_init)

    def forward(self, x):
        x = self.l1(x)
        x = self.l2(x)
        o = self.out(x)
        return o


net = Net()
opt = nn.optim.Adam(net.params, lr=0.1)
loss_fn = nn.losses.MSE()

for _ in range(1000):
    o = net.forward(x)
    loss_ = loss_fn(o, y)
    net.backward(loss_fn)
    opt.step()
    print(loss_)

plt.plot(x, o.data)
plt.show()

