# Regular inflection forms for English high frequency words

This project provides python code to generate the inflectional forms of the most frequent English nouns, verbs, and adjectives for those words that have clear inflectional forms, along as the csv-files resulting from running the code.

The project is mainly of interest to linguists working on English linguistics with only mild or no experience in programming. 

For the first group, it provides a starting point for project tailored to more specific needs, for the second group, it provides the files with all inflectional forms for direct usage.

## Details 

English high frequency words are operationalized here as words with a lemma frequency above 800 in the BNC, itself a 100 million word corpus. This operationalization is already used in the lemmatized list used as an input to the script (see [Lemma source](#lemmataFile)). 

From these lemmata, only those are selected that obey the following constraints:

- Nouns: there are only two clear forms, one for singular, and one for plural. Examples: *course/courses*, *man/men*, *life/lives*. All clear regular s-plurals are included.

- Verbs: there are four clear forms for infinitive, past, gerund, and 3pers singular. Examples: *make/made/making/makes*, *think/thought/thinking/thinks*, *look/looked/looking/looks*. All clear regular verbs are included. Verbs that have different forms for past and perfect participle are not included.

- Adjectives: there are synthetic and clear single comparative and superlative forms. Examples: *new/newer/newest*, *good/better/best*, *royal/royaller/royallest*

The python code is in the file "engInflRegular.py". Paths for input and output data need to be adjusted.

## Third party sources

The project uses two different third party source files that need to be downloaded:

### Lemma source {#lemmataFile}

A pos tagged list of high frequency lemmata from the British National Corpus: "lemma.num" 
The file contains four columns separated by spaces. There is no header.
The columns are: linenummer/rank, frequency, lemma, POS<BR>
Source: :
[Adam Kilgarriff's BNC database and word frequency lists site](https://kilgarriff.co.uk/bnc-readme.html)

### Inflectional forms source {#formsFile}

A list of inflectional forms for English words: "infl.txt"
The file is included in a tar archive available from [AGID (=Automatically Generated Inflection Database)](http://wordlist.aspell.net/other/), the file is (http://downloads.sourceforge.net/wordlist/agid-2016.01.19.tar.gzip)

## Output 

3 comma-separated files of the most frequent English nouns, adjectives, and verbs and their inflectional forms, obeying the restrictions outlined above

1. "bncCoreNounsSgPl.csv": 3088 sg/pl pairs of nouns, comma-separated with headers "sg" and "pl" 

2. "bncCoreVerbsInfPastIng3Sg.csv": 1112 inf/past/gerund/thirdPersonSg quadruplets comma-separated with headers "plain", "past", "gerund", and "thirdSg"


3. "bncCoreAdjectivesPosCompSup.csv": 308 positive/comparative/superlative triplets, comma-separated with headers "pos", "comp", and "sup"


