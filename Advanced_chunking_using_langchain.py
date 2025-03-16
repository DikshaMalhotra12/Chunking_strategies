from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

# Example Text: A short excerpt from a Wikipedia article about Albert Einstein
text = """
## Early life and education

Albert Einstein was born in Ulm, in the Kingdom of Württemberg in the German Empire, on 14 March 1879. His parents were Hermann Einstein, a salesman and engineer, and Pauline Koch. In 1880, the family moved to Munich, where Einstein's father and his uncle Jakob founded Elektrotechnische Fabrik J. Einstein & Cie, a company that manufactured electrical equipment based on direct current.

## Scientific career

In 1900, Einstein was awarded the Federal Polytechnic teaching diploma.  After graduating, Einstein spent almost two years searching for a teaching post. He acquired Swiss citizenship in February 1901, which he kept for his entire life. Through the influence of Marcel Grossmann's father, he secured a job in Bern at the Federal Office for Intellectual Property, the patent office, as an assistant examiner – level III.  He evaluated patent applications for a variety of devices including a gravel sorter and an electromechanical typewriter.
"""
# Splitting by 500 characters with 100 character overlap
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_text(text)
print(f"Number of chunks: {len(chunks)}")
print(chunks[0])
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""] #Prioritize splitting by double newline, then single newline and so on.
)
chunks = text_splitter.split_text(text)
print(f"Number of chunks: {len(chunks)}")
print(chunks[0])
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=["##"]) # Split on h2 headers.
md_chunks = markdown_splitter.split_text(text)
print(f"Number of chunks: {len(md_chunks)}")
print(md_chunks[0])
from langchain.text_splitter import TokenTextSplitter

text_splitter = TokenTextSplitter(chunk_size=100, chunk_overlap=0) # chunks of ~100 tokens.
chunks = text_splitter.split_text(text)
print(f"Number of chunks: {len(chunks)}")
