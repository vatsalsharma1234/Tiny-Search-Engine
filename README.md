# Tiny Search Engine

A simple **Search Engine implementation using an Inverted Index**, built to demonstrate core **Data Structures and Algorithms** concepts used in modern search systems.

The project indexes a collection of documents and allows users to perform fast keyword-based searches with basic relevance ranking.

---

## Overview

Search engines must retrieve relevant information quickly from large datasets.

Instead of scanning every document during a search, this project builds an **inverted index** that maps words to the documents that contain them.

When a user searches for a keyword, the system directly retrieves the relevant documents from the index, making the search much faster.

---

## Features

- Document indexing  
- Fast keyword search  
- Inverted index implementation  
- Frequency-based result ranking  
- Efficient search using hash maps  

---

## How It Works

### 1. Document Indexing

Each document is processed and broken into individual words.

An **inverted index** is created:


word → list of documents containing that word


Example:


data → doc1, doc3
algorithms → doc1, doc3
search → doc2


---

### 2. Query Processing

When a user searches for a word:

1. The word is looked up in the index.  
2. Relevant documents are retrieved.  
3. Documents are ranked based on word frequency.  
4. Results are returned.

---

## Example

### Documents


doc1: data structures and algorithms
doc2: search engine using inverted index
doc3: algorithms and data science


### Search Query


algorithms


### Result


doc1
doc3


---

## Tech Stack

- **C++**
- **STL** (`unordered_map`, `vector`, `string`)
- Basic text processing

---

## Data Structures Used

- Hash Map
- Vector
- String processing
- Sorting algorithms

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Indexing | O(N × W) |
| Search | O(K log K) |

Where:

- **N** = number of documents  
- **W** = average words per document  
- **K** = number of documents containing the query word  

---
