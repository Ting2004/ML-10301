---
typora-copy-images-to: ./assets
---

# Overfitting



1/27/2025

___



## Overfitting

- is too complex
- is fitting the noise in the data or fitting “outliers”
- does not have enough bias
- true error rate is larger than the training error rate



### Validation set (decision tree)

- grow the tree (training) with training set
-  evaluate each split using the validation
  - compare the validation error rate with and without the split
  - remove the split that most decreases the validation error rate
  - stop if no split improves validation error



### Decision Tree DT

- very easy to explain
- very efficient
- could be used for classification, regression, density estimation...

