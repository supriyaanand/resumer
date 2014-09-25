__author__ = 'suanand'

import nltk
from nltk.tokenize import sent_tokenize

class Resumer:

    def __init__(self):
            self.tokens = []
            self.subCats = {}
            self.freqDist = {}
            self.max_summary_size = 500   # number of words/tokens

    def tokenize(self):
        self.tokens = nltk.word_tokenize(self.input)


    def tokenize_sentence_to_words(self,sentence):
        sent_tokens = nltk.word_tokenize(sentence)
        return sent_tokens

    def getFreqDist(self):
        for word in self.tokens:
            try:
                self.freqDist[word] = self.freqDist[word] + 1
            except KeyError:
                self.freqDist[word] = 1

    def sentence_tokenizer_from_text(self):
        self.tokenized_sent_list = sent_tokenize(self.input)

    def sentence_score(self,sentence):
        return sum((self.freqDist[token] for token in self.tokenize_sentence_to_words(sentence)))


    def create_summary(self):
        summary = []
        size = 0
        for sentence in self.tokenized_sent_list:
            summary.append(sentence)
            size += len(sentence)
            if size >= self.max_summary_size:
                break

        summary = summary[:self.max_summary_size]
        return '\n'.join(summary)


    def summarize(self):
        self.tokenize()
        self.getFreqDist()
        self.sentence_tokenizer_from_text()
        self.tokenized_sent_list.sort(key=lambda s: self.sentence_score(s), reverse=1)
        self.summary = self.create_summary()

        return self.summary



if __name__ == '__main__':
    R = Resumer()
    R.input = '''Automatic summarization is the process of reducing a text document with a computer program in order to create a summary that retains the most important points of the original document. As the problem of information overload has grown, and as the quantity of data has increased, so has interest in automatic summarization. Technologies that can make a coherent summary take into account variables such as length, writing style and syntax. An example of the use of summarization technology is search engines such as Google. Document summarization is another.

Generally, there are two approaches to automatic summarization: extraction and abstraction. Extractive methods work by selecting a subset of existing words, phrases, or sentences in the original text to form the summary. In contrast, abstractive methods build an internal semantic representation and then use natural language generation techniques to create a summary that is closer to what a human might generate. Such a summary might contain words not explicitly present in the original. Research into abstractive methods is an increasingly important and active research area, however due to complexity constraints, research to date has focused primarily on extractive methods.Extraction techniques merely copy the information deemed most important by the system to the summary (for example, key clauses, sentences or paragraphs), while abstraction involves paraphrasing sections of the source document. In general, abstraction can condense a text more strongly than extraction, but the programs that can do this are harder to develop as they require the use of natural language generation technology, which itself is a growing field.

While some work has been done in abstractive summarization (creating an abstract synopsis like that of a human), the majority of summarization systems are extractive (selecting a subset of sentences to place in a summary). Two particular types of summarization often addressed in the literature are keyphrase extraction, where the goal is to select individual words or phrases to "tag" a document, and document summarization, where the goal is to select whole sentences to create a short paragraph summary.'''
    print R.summarize()








