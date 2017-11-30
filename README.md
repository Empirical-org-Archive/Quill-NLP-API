# Quill NLP API

This is where we make our NLP apis accessible.

Routes

post /get_POS/ {text: "A sentence with a bunch of things."}
returns the POS tags for the sentence in an array

post /sentence_or_not/ {text: "A sentence with maybe something missing."}
returns a floating point number indicating the likelyhood the sentence is a sentence 1.0 being the best, 0.0 being the worst.

get /ping/
returns 200 ok if the server is alive.