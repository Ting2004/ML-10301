---
typora-copy-images-to: ./assets
---

# Perceptron

1/31/25

___



### Linear Algebra

vector representation
$$
w_1x_1 + w_2x_2 + b = 0
$$
then the weight vector $[w_1, w_2]^T$ will be orthogonal to the line specified





### Online Learning

- $t = 1,2,3\dots$

- receive a unlabeled input $x^{(t)}$

- make a prediction $\hat{y} = h_{w, b}(x^{(t)})$
- compare with true label $y^{(t)}$ and penalty if not the same
- update $w$ and $b$





### Perceptron Training (online, no bias)

- take a point, make a random guess
  - if correct, do nothing
  - if incorrect
    - measure the vector from the origin to the point
    - flip it
    - make a line through the origin that is orthogonal to it
  -  repeat until converge









