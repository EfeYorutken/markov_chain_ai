# What is this?
This is a simple project displaying the text generation capabilities of a markov chain based _artificial intelligence_

## What is a markov chain?
> Disclaimer: I am not a mathematician, nor an expert on markov chains, artificial intelligence or language models. This is a very rudementary explanation according to my limited  understanding.

Markov chains are graph-like representations of probability. They display probability of some event occurring (transitioning to a state) given the status quo (current state).
This way of relating 2 states in terms of how likely one is to come after the other can be very useful for generating coherent text. As a matter of fact, this is how most text LLMs work.

## How does it work
Given a large enough coherent text. This text will involve certain word combinations like
    - I am
    - there is
    - public static void
more frequently compared to other combinations such as
    - maybe there
    - will have
    - world matrix
More a given word pair is used, the more likely it is to appear in the text. As a result of this appearance a markov chain can be created where each word is connected to all other keys based on how likely
the second word appears after the first. Iterating over the markov chain based on this likelihood should create grammatically coherent and even sensible sentences.
