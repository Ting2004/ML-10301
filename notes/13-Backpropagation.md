---
typora-copy-images-to: ./assets
---

# Backpropagation

2/19/25 & 2/24/25

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
- procedure
  - run a forward path
  - differentiate backwards
    - no repeated computation
    - efficient because a lot of reuse

  - until reach the input
  - descent :)






### Finding Gradient for NN

convention: *denominator layout*

the shape of derivative is aways the same shape as the denominator

![image-20250224111459577](./assets/image-20250224111459577.png) 





#### target

find the derivative of all the weights with respect to the result

![image-20250224113456646](./assets/image-20250224113456646.png)



In general, we need to find

![image-20250224113517314](./assets/image-20250224113517314.png)

for each $a, b$

