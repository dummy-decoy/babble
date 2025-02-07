# babble
A Python WSGI application which uses Markov chains to generate an infinitely long nonsensical babble.

A live demo is available at [https://stochastique.io/babble/](https://stochastique.io/babble/)

### The markov Python module
The markov Python module (`markov.py`) implements a basic Markov chain babbler. 

Import the module, then call its __`build()`__ function, passing it a string containing the corpus from which the module will construct its database. You can call the `build()` function multiple times to add to the corpus. The __`split()`__ function does the heavy lifting of tokenizing the input into words or punctuation and ignoring spaces. The __`babble()`__ function is a generator which will spit tokens to be concatenated in order to form the output text.

The __`context_size`__ global variable controls the number of words forming the context for chosing the next word. It is used while building the database and generating the output babble, don't change it carelessly. By default, the babbler is using _3_ words of previous context, just because i find it generates more cohesive sentences. You can play and find the setting which fit the most for your use, but beware that a value set too high will just spit the corpus as is.  

The __`database`__ global variable is the database of all context words, suit and occurences. It lives in memory and can become pretty huge. 

The __`starts`__ global variable holds all word sequences starting a sentence. It is used to start the babbler with words having a meaning at the beginning of a sentence. Maybe I should make a better use of its content...

### The server Python module
The server Python module (`server.py`) implements the WSGI application.

It imports the markov module and builds its database using the __`corpus.txt`__ file. 

When a client accesses the application, the application outputs an html page containing a never-ending babble, formatted as html with randomly spaced paragraph delimiters. The application ignores any request parameter or URL access path. The output never ends: the only way to stop generating content is to end the connection to the server.

The __`babbler()`__ function is a generator function consuming the markov babbler and formatting the output. The __`markov_babble()`__ function is the WSGI application itself.

The __`throttle`__ global variable controls the amount of time, expressed in seconds, the application sleeps between each word output. This allows to gently babble without overloading the server. 

### The corpus
The __`corpus.txt`__ file is used to build the database when starting the application. The included corpus is poorly build from selected works of _Mark Twain_. That's a bit limited, build your own corpus, experiment...

## Running the application

You will need a WSGI host, like `waitress`, `uWSGI`, `Green Unicorn`, `mod_wsgi`, ...
