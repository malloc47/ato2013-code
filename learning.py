# adapted from http://scikit-learn.org/stable/auto_examples/plot_digits_classification.html
import sys
from skimage.viewer import ImageViewer
from sklearn import datasets, svm, metrics

sys.tracebacklimit = 0

# load built-in dataset
digits = datasets.load_digits()

print(digits.target[0])
ImageViewer(digits.images[0]).show()

print(digits.target[5])
ImageViewer(digits.images[5]).show()

print(digits.target[9])
ImageViewer(digits.images[9]).show()

n = len(digits.images)
data = digits.images.reshape((n, -1))

data_first_half = data[:n / 2]
target_first_half = digits.target[:n / 2]

data_second_half = data[n / 2:]
target_second_half = digits.target[n / 2:]

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# train on first half
classifier.fit(data_first_half, target_first_half)

# predict second half
predicted = classifier.predict(data_second_half)

# see some metrics
print("Report:")
print("%s\n" % metrics.classification_report(target_second_half, predicted))
print("Confusion matrix:")
print(metrics.confusion_matrix(target_second_half, predicted))

# try some out
print(classifier.predict(data_second_half[1])[0])
ImageViewer(digits.images[n/2+1]).show()

print(classifier.predict(data_second_half[2])[0])
ImageViewer(digits.images[n/2+2]).show()

print(classifier.predict(data_second_half[3])[0])
ImageViewer(digits.images[n/2+3]).show()
