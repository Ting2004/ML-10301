---
typora-copy-images-to: ./assets
---

# Neural Networks

2/17/25 & 2/19/25

___

intuition: combine perceptrons to achieve non-linear decision boundary

![image-20250217113153239](./assets/image-20250217113153239.png)



modify the Boolean algebra into weights and operations

- $AND(z_1, z_2) = sign(z_1 + z_2 - 1.5)$
- $OR (z_1, z_2) = sign(z_1 + z_2 + 1.5)$
- $NOT(z) = -1 \cdot z$

![image-20250217114214290](./assets/image-20250217114214290.png)







### Notations

- $D$ dimension
- $L$ Layers
- $w$ weights

![image-20250217115849947](./assets/image-20250217115849947.png)

![image-20250217120007028](./assets/image-20250217120007028.png)







### Loss Function and Objective Function

![image-20250219110918613](./assets/image-20250219110918613.png)

notice that output of layer (D) is a real number but the final output after layer (E) is a probability $\in [0, 1]$



#### Quadratic Loss

- same as Linear regression
- MSE

$$
\begin{align*}
J &= l_Q (y, y^{(i)}) = \frac{1}{2} (y - y^{(i)})^2\\
&\frac{dJ}{dy} = y - y^{(i)} 
\end{align*}
$$



#### Binary Cross-Entropy

- same as Binary Logistic Regression
  - negative log likelihood
  - output would be $\in [0, 1]$
- have steeper gradient than quadratic loss

$$
\begin{align*}
J &= l_{CE} (y, y^{(i)}) = -(y^{(i)}\log{y} + (1 - y^{(i)})\log{(1-y)})\\
&\frac{dJ}{dy} = - (y^{(i)} \frac{1}{y} + (1-y^{(i)})\frac{1}{y-1})
\end{align*}
$$



### Multiclass Output

- softmax

$$
y_k = \frac{\exp{b_k}}{\sum_{l=1}^K \exp{b_l}}
$$







> one-hidden layer neural network is a *universal function approximator*
