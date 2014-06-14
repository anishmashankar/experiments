import random
from nltk.corpus import movie_reviews
from text.classifiers import NaiveBayesClassifier
random.seed(1)
 
train = [
('I love this sandwich.', 'pos'),
('This is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('This is my best work.', 'pos'),
("What an awesome view", 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('He is my sworn enemy!', 'neg'),
('My boss is horrible.', 'neg')
]
test = [
('The beer was good.', 'pos'),
('I do not enjoy my job', 'neg'),
("I ain't feeling dandy today.", 'neg'),
("I feel amazing!", 'pos'),
('Gary is a friend of mine.', 'pos'),
("I can't believe I'm doing this.", 'neg')
]
print 'initial training going on....'
cl = NaiveBayesClassifier(train)
print 'initial training done.'
# Grab some movie review data
print 'now gathering reviews...'
reviews = [(list(movie_reviews.words(fileid)), category)
for category in movie_reviews.categories()
for fileid in movie_reviews.fileids(category)]
random.shuffle(reviews)
new_train = reviews[0:200]
print 'reviews gathered.'
# Update the classifier with the new training data
print 'now training using the new data...'
cl.update(new_train)
print 'trained and ready!'
print cl.classify("I hated the movie and hated the food")
# Compute accuracy
accuracy = cl.accuracy(test)
print("Accuracy: {0}".format(accuracy))