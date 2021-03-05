from nltk.corpus import stopwords
import string


class TextOutlier:

    def remove_punctuation(self, data=[]):
        """
        remove punctuation
        """
        clean_text = []

        for text in data:
            try:
                sentences = text.lower()
                for c in string.punctuation:
                    sentences = sentences.replace(c, "")
                clean_text.append(sentences)
            except:
                pass
        return clean_text

    def remove_stopwords(self, data=[], lang="english"):
        """
        removing stop words ex: The, is, a
        """
        clean_text = []
        # remove stop words

        for text in data:
            sentences = text.lower().split()
            free_sw = []
            result = ''
            for sw in sentences:
                if sw not in stopwords.words(lang):
                    free_sw.append(sw)

            # merge words
            for words in free_sw:
                result += words + " "
            result = result[0:len(result) - 1]

            clean_text.append(result)

        return clean_text
