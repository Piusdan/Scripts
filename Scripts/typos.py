#! python3
# program to find common typos e.g multiple spaces between words, accidental
# repeated words multiple eclamation marks at the end of a sentance
import re
import pyperclip


def autoCorrect():
    # get text from clipboard
    text = pyperclip.paste()
    text = str(text)
    # replace multiple spaces
    print('Checking multiple spaces...')
    text = re.sub(r'(\s+){2,}', ' ', text)
    print('Done')
    # replace multiple punctiation marks
    print('Checking punctuation...')
    text = re.sub(r'([!.,?])([!.,?]*)', r'\1', text)
    print('Done')
    # replace accidental repeated words
    print('Checking repeated words...')
    text = re.sub(r'\b(\w+)\s\1\b', r'\1', text)
    print ('Done')
    # copy tet to clipboard
    pyperclip.copy(text)
    # End
    print('Editing done succesfully')
if __name__ == '__main__':
    autoCorrect()
