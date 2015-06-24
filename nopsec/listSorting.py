import argparse
import os
import re
import sys
from collections import OrderedDict


class list_sorting(object):
    """ Class sorts a list based on its type of data and writes to output file
    For example: 1, 5, dog, 3, cat, 0
    Results in:  0, 1, cat, 3, dog, 5

    Command line arguments:
        Input file, Output file
    Other Notes:
        Output file must not exist already.
    """

    def __init__(self, input_file, output_file):
        """ Initializes the list sorting.
        Checks to see if input file exists and output file do not exist.
        Then stores global variables for their respective values.
        """

        if not os.path.isfile(input_file):
            sys.exit('Error: input_file does not exist!')

        if os.path.isfile(output_file):
            sys.exit('Error: output_file already exists!')

        self.input_file = input_file
        self.output_file = output_file

    def parse_data(self):
        """ Creates two dictionaries that save the word and its position. """
        self.words = {}
        self.numbers = {}

        word_count = 0

        """ Build a string by reading character by character. """
        with open(self.input_file, "rb") as f:
            string_builder = ""
            char = f.read(1)

            if not char:
                sys.exit('Error: Empty file!')

            while char:
                string_builder += char

                char = f.read(1)

                """ When you arrive at a space, add the character to your
                word or number dicts after you strip any illegal characters.
                Cast to integer if need be. Negative signs are manually added.
                """

                if char == " " or char == '\n' or (not char):
                    """ Replace everything but the '-' and alphanumericals
                    Then, replace any dashes that are not in the 0th spot.
                    If this is an edge case of a string, replace the first
                    dash as well. Then, pass to dictionary, reset the word
                    and move onto reading the next character.
                    """
                    string_builder = re.sub('[^-a-zA-Z0-9]', '',
                                            string_builder)

                    string_builder = string_builder[0] + string_builder[1:].replace("-", "")

                    if string_builder[1:].isalpha() and string_builder[0] == '-':
                        string_builder = string_builder[1:]

                    if string_builder.isalpha():
                        self.words[word_count] = string_builder
                    else:
                        self.numbers[word_count] = int(string_builder)

                    string_builder = ""
                    word_count += 1
                    char = f.read(1)

    def sort_data(self):
        """ Data is sorted by sorting dictionaries values,
        then zipping over both the sorted values and updating
        their position in the original dictionary.
        This is done for both the numbers and loops dictionaries.
        The comparator used for the string is compared in the lambda.
        """

        for (sorted_key, sorted_value), (original_key) in zip(sorted(
                self.words.items(), key=lambda x: x[1].lower()), self.words.keys()):
            self.words[original_key] = sorted_value

        for (sorted_key, sorted_value), (original_key) in zip(sorted(
                self.numbers.items(), key=lambda x: x[1]), self.numbers.keys()):
            self.numbers[original_key] = sorted_value

        """ Here, the dictionaries are merged and the second one is emptied."""
        self.words.update(self.numbers)
        self.numbers.clear()

    def write_data(self):
        """ Data is written from the dictionary to the output file.
        """
        final_string = ""
        last_word = len(self.words) - 1

        """ This loop creates the final string from the dictionary and is sorted
        in order of the keys. The loop appends spaces up until the final word.
        """

        for (k, v) in sorted(self.words.items()):

            if k == last_word:
                final_string += str(self.words[k])
                continue

            final_string += str(self.words[k]) + ' '

        """ Finally, we check again if the file does not
        exist before we write the final_string to the file.
        """

        if not os.path.isfile(self.output_file):
            with open(self.output_file, "w+") as f:
                f.write(final_string)
        else:
            sys.exit("Error: output_file already exists!")

if __name__ == '__main__':
    """ The argparse module allows me to easily pass in the variables to
    the class wihle ensuring the user provides two variablies and has
    documentation available to them if they do not provide the proper input.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('input_file', help='Specify the input filename')
    parser.add_argument('output_file', help='Specify the output filename')

    res = parser.parse_args()

    ls = list_sorting(res.input_file, res.output_file)

    ls.parse_data()
    ls.sort_data()
    ls.write_data()
