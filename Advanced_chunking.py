import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt_tab')
nltk.download('stopwords')  # Download necessary NLTK data

# Example Text (a paragraph from Wikipedia about Albert Einstein)
text = "Albert Einstein was born in Ulm, Germany, in 1879. He developed the theory of relativity, one of the two pillars of modern physics (alongside quantum mechanics). His work is also known for its influence on the philosophy of science. He is best known to the general public for his mass–energy equivalence formula E = mc², which has been dubbed 'the world's most famous equation'. He received the 1921 Nobel Prize in Physics 'for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect', a pivotal step in the development of quantum theory."


# 1. Sentence Chunking
sentences = sent_tokenize(text)
print("Sentence Chunking:")
for i, sentence in enumerate(sentences):
    print(f"Chunk {i+1}: {sentence}")

# 2. Paragraph Chunking (Assuming our text is a single paragraph for this example)
paragraphs = [text] # In real scenarios, split by '\n\n'
print("\nParagraph Chunking:")
for i, paragraph in enumerate(paragraphs):
    print(f"Chunk {i+1}: {paragraph}")



# 3. Sliding Window with Overlap
def sliding_window(text, window_size, overlap):
    sentences = sent_tokenize(text)
    chunks = []
    for i in range(0, len(sentences) - window_size + 1, window_size - overlap):
        chunk = " ".join(sentences[i:i + window_size])
        chunks.append(chunk)
    return chunks

window_size = 2  # Example: 2 sentences per chunk
overlap = 1      # Example: 1 sentence overlap
chunks = sliding_window(text, window_size, overlap)
print("\nSliding Window Chunking:")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")


# 4. Recursive Splitting (Simplified example using headings; real-world scenarios would involve parsing document structure)
headings = ["Early Life", "Scientific Contributions", "Later Life"]  # Imagine these are extracted from a document
sections = text.split(". ") # Very simplified splitting, just for illustration.  Real-world examples would use proper section delimiters
# In real applications, map sections to headings based on document structure.

print("\nRecursive Splitting (Simplified):")
for i, (heading, section) in enumerate(zip(headings,sections[:len(headings)])): # Limit sections to available headings
    print(f"Chunk {i+1} ({heading}): {section}.")


import spacy

### Run python -m spacy download en_core_web_sm in command prompt

nlp = spacy.load("en_core_web_sm")

def chunk_with_spacy(text):
    doc = nlp(text)
    chunks = []
    for sentence in doc.sents:
        chunks.append(sentence.text) # Use Spacy's sentence segmentation for now
    return chunks

spacy_chunks = chunk_with_spacy(text)
print("\nSpacy Chunking:")
for i, chunk in enumerate(spacy_chunks):
    print(f"Chunk {i+1}: {chunk}")