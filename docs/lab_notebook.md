#Lab Notebook

## 2016-12-26
Creating repo, writing readme

A couple of thoughts to wrangle:
 - Which packages? (sklearn api, numpy, andpandas seem likely)
 - How to test?
 - Which aglorithms first?
 
Settled on using Chase Sapphire Reserve (CSR) dataset from reddit. Is this a legal issue?

Looking at my previous implementation
 - [In this private repo](https://github.com/USF-MSAN621-F14/bjherger-ML1-proj/tree/master/algorithm2-decision_tree)
 - Should make this public
 
From "Tree-Based Methods" in ISL:
 - Minimize residual sum of squares (RSS)
 - How will I choose the cutoff point? Mean or median seems easiset.
  
It will be easier to use Pandas for X and y input, rather than allowing for numpy matrices

I'm forgoing pruning until a later iteration. 

Writing regression and classification trees separately. I'll do classificaiton first.

Usinr 9.2.3 Classification Trees of ESL 

skipping implementing sklearn estimator interface
  
