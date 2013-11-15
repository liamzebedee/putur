# Putur
Putur generates statistically similar words to a corpus and puts them in a phrase using a Markov chain. The implementation is based off [this blog post](http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/) by Shabda Raaj.

`python markov.py`

## Introduction
The idea is simple: instead of using words to generate statistically similar sentences, I use letters to generate statistically similar words to the corpus. I've supplied the contents of Obama's re-election speech from 2012 as a default corpus for the algorithm. Here are some examples:

> diblis their voicaught yeance lonever we re lover wit a com as abled I've warick me Stand tracho mationget not of hose ample fat
> he of fory cand come the theal cy Ame re. Thattenthroole, not ma goince. Ton 200 youghted ismovervidestry fork on oureed ide fo
> on of thethe will publeyour of to do jus than ought. I witin figace st yought. I heir of your thatin thromner cy haver def your

## Notes
While you see there are some similarities in the pronunciation of the words, it is not perfect. With a bigger corpus size you might see some differences. It is worthy to note that I operate on characters. If there was a good syllable parsing library maybe putur could be improved.

It's also interesting to note that you can change the corpus to texts from other languages, as putur is purely based on statistical correlations between letters.

I did this as part of an assessment piece on Markov chains. You can read [the paper](https://github.com/liamzebedee/putur/blob/master/MarkovChains.pdf) for a general explanation.
