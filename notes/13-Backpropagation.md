---
typora-copy-images-to: ./assets
---

# Backpropagation

2/19/25

___

### Differentiation

- let $f : \mathbb{R}^A \rightarrow \mathbb{R}^B$
- and we want to find $\frac{\delta f(x)_i}{\delta x_j} \forall i, j : A \times B$

![image-20250219114623341](./assets/image-20250219114623341.png)![image-20250219114702262](./assets/image-20250219114702262.png)



#### Finite Difference Method

- find gradient given a small step $\epsilon$

- Suffers from issues of floating point precision, in practice
- Typically only appropriate to use on small examples with an appropriately chosen $\epsilon$

![image-20250219115139188](./assets/image-20250219115139188.png)



### Backpropagation

- chain rule :)











