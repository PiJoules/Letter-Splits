# Letter Splits
https://www.reddit.com/r/dailyprogrammer/comments/3xye4g/20151223_challenge_246_intermediate_letter_splits/

## Usage
```py
$ python main.py 1252020518
Regular: set(['LEBBEAH', 'ABETBER', 'ABETTEAH', 'ABETBEAH', 'AYBBEAH', 'ABEBBER', 'ABEBTER', 'AYBBER', 'LEBTER', 'AYBTEAH', 'LETBER', 'LETTEAH', 'ABETTER', 'LETTER', 'LEBBER', 'ABEBBEAH', 'AYTBEAH', 'AYBTER', 'LEBTEAH', 'ABEBTEAH', 'AYTTEAH', 'AYTTER', 'AYTBER', 'LETBEAH'])
Using real words: set(['ABETTER', 'LETBEAH', 'ABETBEAH', 'ABEBBER', 'LETTER'])
```
When using real words, I only check if the string constains consecutive substrings of words provided in `enable1.txt`. For this script, the words to not need to form a proper sentence, they just need to exist in the txt file.