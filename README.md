# Naive-Bayes-Classifier
A Naive-Bayes classifier based model for binary classification among blogs. It uses frequency of occurrence of the words in vocabulary to classify the blog category. 
It performs smoothing to avoid 0 probability of unseen words in a test blog.
The model is also parametrized to remove top N most frequent words in the vocabulary to account of language specific filler words which doesn't carry any specific information around the classification.
