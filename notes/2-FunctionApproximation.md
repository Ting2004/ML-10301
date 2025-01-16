# Machine Learning as Function Approximation

1/15/2025

___



idea: use a simple function to approach a more complicated shape



### Example - Supervised Binary Classification

supervised: dataset present features and **corresponding labels**



#### Setup

- $X$ as the set of all inputs (feature vectors)
- $Y$ as the set of all outputs (labels)

- $C^*$ as the unknown target function
  - $C^* : X \rightarrow Y$
  - e.g. $C^* : \mathbb{R}^3 \rightarrow \mathbb{R}$
- $H$ as a set of hypothesized functions
  - $H = \{h \mid h : X \rightarrow Y\}$



- a **learner** is given dataset $D = \{(\vec{x}^{(1)},y^{(1)}), (\vec{x}^{(2)},y^{(2)})\cdots \}$ of a known target function $y^{(i)} = C^*(\vec{x}^{(i)})$ for all $i \in \{1, 2,\cdots N\}$, where $N$ is the size of dataset
- a learner produces hypothesis $h \in H$ that *best approximate* $C^*$ given $D$
- a **loss function** $l : y \times y \rightarrow \mathbb{R}$ measures how *bad* predictions $\hat{y} = h(\vec{x})$ are compared to true values $y^* = C^*(\vec{x})$
- a **test set**  $D_{test} = \{(\vec{x}^{(1)},y^{(1)}), (\vec{x}^{(2)},y^{(2)})\cdots \}$ and we evaluate the average loss of $h(\vec{x})$ on the test set







### Evaluation Functions

- squared loss 

  - for regression
  - $l(\hat{y}, y^*) = (\hat{y} - y^*)^2$

- binary loss

  - for classification
  - $l(\hat{y}, y^*) = \mathbb{1}(\hat{y}\ne y^*)$
  - if not equal then 1 else 0

### Error Rate

- **train** error rate
- **test** error rate
- **true** error rate
  - real error rate when encountering future data (inaccessible!)
  - we want the model to work well with the distribution of *future* data