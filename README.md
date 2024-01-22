# emberosaurus

Emberosaurus is an LM-based thesaurus for the English language. It uses [WordNet](https://wordnet.princeton.edu/) lexical database and the [spaCy](https://spacy.io/) NLP library to generate synonyms for words and then ranks them within the given context using [Ember](https://huggingface.co/llmrails/ember-v1), a Sentence Transformer model.

## Credits

This project is mostly a rework of [Bertosaurus](https://github.com/cedricconol/bertosaurus/tree/master). The main difference is that Emberosaurus uses a different LM and updated models in general, which should make it more accurate.

## Requirements

- You will need a recent-enough version of Python 3 installed on your system. The code was tested with Python 3.11.5 specifically.

- About 2 GB of free disk space and at least 2 GB of RAM are required to run the program (can be reduced by using a smaller spaCy model).

## Installation

You can either download the code manually or clone the repository using git, like so:

```bash
git clone https://github.com/marcodsn/emberosaurus.git
```

Next, you need to install the required dependencies. You can do this by running the following command in the root directory of the project:

```bash
pip install -r requirements.txt
```

You will also need to manually download the spaCy model that will be used by the program. You can do this by running the following command:

```bash
python -m spacy download en_core_web_trf
```

## Usage

### CLI

To use Emberosaurus, you can run and interact with it directly from the command line, like so:

```bash
python cli.py
```

When prompted, enter a sentence and a word from that sentence that you want to find synonyms for. Here is an example:

```bash
Input a sentence: The quick brown fox jumps over the lazy dog
Input a word: quick

fast (0.517)
speedy (0.514)
immediate (0.506)
straightaway (0.493)
ready (0.491)
agile (0.488)
prompt (0.487)
spry (0.477)
nimble (0.473)
warm (0.462)
flying (0.459)
Input a sentence:
```

The program will then print out the available synonyms for the given word, along with their Ember scores (the closer to 1 the better).

To exit the program, simply press `Ctrl+C`.

### API

You can also run Emberosaurus as a web service. I included a simple Flask app that you can use to do this. To start the server, run the following command in the root directory of the project:

```bash
python server.py
```

A simple client is also included, and it can be run like so:

```bash
python client.py
```

The context sentence and the base word are hardcoded in the client, as it is only meant to be used as an example. Modify the code to suit your needs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
