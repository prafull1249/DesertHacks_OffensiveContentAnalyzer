## Inspiration
Nowadays, aggressive websites with highly offensive content are not uncommon to find as we browse through the convoluted network of hyperlinks on the internet. Moreover, it is highly accessible for the small children to come across such sites and discover such content. This aggressive content might impact small children in inappropriate ways. Therefore, safeguarding small children from such content is need of the hour. This motivated us to develop a chrome plugin to block websites based on its text's offensive quotient. 

## What it does
The chrome plugin blocks websites warning that the text in the website has high offensive quotient. It also provides to select and a particular text and measure its offensive content, semantic tone and language used.

## How I built it
We built a python module which did natural language processing using nlp techniques like pos tagging, lemmatization, bag of words, similarity measurement using word2vec predominantly to measure the offensive quotient. 
Bag of words was maintained of all the offensive and negative words. It is compiled from two main resources. 
    racial slur database organisation.
    offensive words in English by CMU.

We also used Alchemy API from IBM to measure the semantic tone, mood and language used in the text. This were supposed to be integrated together in a chrome plugin.

## Challenges I ran into
The word2vec model being used is around 3.25GB binary file and therefore using it at once in the system created lags and prevented us to integrate the python module.

## Accomplishments that I'm proud of
We got a decent amount of accuracy while measuring the offensive content of the text. For example, 


## What I learned
Chrome plugin building, New techniques to mine text and measure offensive quotient, Alchemy API, 


## What's next for HarassmentAnalyser
Offensive content analysers can be integrated as a plugin similar to adblocker. We can measure the overall offensive content on the website especially on forums and comments section to measure the offensive and aggressive content. 
