
# Advanced Chunking Strategies for Retrieval Augmented Generation (RAG)

This repository explores and implements advanced chunking strategies for optimizing retrieval in Retrieval Augmented Generation (RAG) pipelines.  It provides both custom Python implementations and leverages the LangChain library for more advanced and flexible chunking.

## Contents

* **`advanced_chunking.py`**: Contains custom Python implementations of various chunking strategies, including:
    * Sliding window chunking with overlap
    * Recursive splitting based on document structure
    * Chunking by semantic units (paragraphs, headings)
* **`advanced_chunking_using_langchain.py`**: Demonstrates the use of LangChain's `TextSplitter` for various chunking methods:
    * `CharacterTextSplitter`
    * `RecursiveCharacterTextSplitter`
    * `MarkdownHeaderTextSplitter`
    * `TokenTextSplitter`
* **`requirements.txt`**: Lists the required Python packages for running the code.
* **`README.md`**: This file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com//DikshaMalhotra12/Chunking_strategies.git
