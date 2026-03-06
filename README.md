Tiny Search Engine (Inverted Index + Ranking)

A lightweight Search Engine implemented using core Data Structures and Algorithms.
This project demonstrates how search systems index documents and retrieve relevant results efficiently using an Inverted Index.

The system processes a collection of documents, builds an index mapping words → documents, and supports fast search queries with simple frequency-based ranking.

This project simulates the fundamental concepts used in large-scale search systems such as Google Search.

Features

Builds an Inverted Index for fast search

Supports keyword-based queries

Returns documents ranked by word frequency

Efficient lookup using Hash Maps

Handles multiple documents and queries

Demonstrates real-world information retrieval concepts

System Design Overview

The search engine works in two phases:

1. Indexing Phase

Documents are processed and broken into individual words.

Each word is stored in an inverted index structure:

word → list of documents containing that word

Example:

data → doc1, doc3
algorithms → doc1, doc3
search → doc2

This allows very fast lookups during search.

2. Query Phase

When a user enters a search query:

The system looks up the word in the index.

Retrieves all documents containing the word.

Ranks them by frequency of occurrence.

Returns the most relevant results.

Example

Documents:

doc1: data structures and algorithms
doc2: search engine using inverted index
doc3: algorithms and data science

Query:

search: algorithms

Output:

doc1 (1)
doc3 (1)
Data Structures Used
Data Structure	Purpose
Hash Map	Store inverted index
Vector / List	Store document IDs
String Processing	Tokenize documents
Sorting	Rank results
Time Complexity
Operation	Complexity
Indexing Documents	O(N × W)
Search Query	O(K log K)

Where:

N = number of documents

W = average words per document

K = number of documents containing the query term

Using an inverted index reduces search time dramatically compared to scanning every document.
