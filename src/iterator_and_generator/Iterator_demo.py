
class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        lindex = self.index
        self.index += 1
        return self.words[lindex]


def sentence_generator(sentence):
    for word in sentence.split():
        yield word


def iterable_And_Iterator_demo():
    # Iterator objects in python conform to the iterator protocol,
    # which basically means they provide two methods: __iter__() and  next().
    # The __iter__ returns the iterator object and is implicitly called at the start of loops.
    # The next() method returns the next value and is implicitly called at each loop increment.
    # next() raises a StopIteration exception when there are no more value to return,
    #   which is implicitly captured by looping constructs to stop iterating.

    sentence = 'This is test'
    mysent = Sentence(sentence)

    # Iterator in action
    for word in mysent:
        print(word)


if __name__ == "__main__":
    iterable_And_Iterator_demo()
