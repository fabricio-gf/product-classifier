Product classifier

This script was made during the selection process of the company Birdie, in July 2019.

It takes a list of various products and classifies each one as Smartphone related or Non-smartphone related, based on pre-defined keywords like "smartphone".

Some considerations and acknowledgement of a few problems present in the code:
- Python is not one of my most familiar languages.
- At first, I thought about using a Naive Bayes classifier, but using probability seemed overkill for this application, and also would require a testing set with known results.

- Possible problem at line 19: All keywords were chosen by me, after a quick scan of the product names and popular smartphone brands. Maybe some automated process for defining keywords would make the results better.
- Possible problem at line 27: I tried to remove accents and special characters (like "ã" to "a", "ç" to "c" and "ô" to "o"). Through some searching, I found these unicode functions, but the end result was not quite as expected. There probably is a better solution that I haven't thought of.
- Possible problem at line 34: I want to check if there is an intersection between the keyword array and the current product's tokens. So I found a solution of putting both arrays into sets, and the & operator. It worked fine, but I don't actually know if this is best on performance and memory allocation.