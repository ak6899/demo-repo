# StudyBot

A Streamlit-based study assistant that converts your uploaded notes into a searchable knowledge base and answers questions using OpenAI.

## What StudyBot does

StudyBot lets you upload notes and then ask natural-language questions about the content. It works by:

- extracting text from uploaded notes
- splitting the content into smaller chunks
- generating semantic embeddings for each chunk
- storing the embeddings in a FAISS vector store
- searching the store for relevant chunks when you ask a question
- using OpenAI to answer the question based on those chunks

## How it works

1. **File upload**
   - The app provides a sidebar file uploader for `.pdf`, `.txt`, and `.docx` files.
   - The current code extracts PDF text with `PyPDF2`, while `.txt` and `.docx` are accepted in the UI.

2. **Text extraction**
   - Uploaded file pages are read and text is extracted from each page.
   - The extracted text is displayed in the app for quick review.

3. **Chunking**
   - The text is split into overlapping chunks using `RecursiveCharacterTextSplitter`.
   - This helps the semantic search engine find the most relevant sections of your notes.

4. **Embeddings**
   - Each text chunk is converted to an embedding vector with `OpenAIEmbeddings`.
   - Embeddings represent meaning in a numerical form.

5. **Vector search**
   - Chunks are stored in a `FAISS` index.
   - When you enter a query, the app performs similarity search over the index.
   - It retrieves the top matching chunks for the question.

6. **Question answering**
   - The selected chunks are passed to a GPT-based QA chain.
   - `ChatOpenAI` generates an answer using the relevant note content.
   - The model is configured with `gpt-4o-mini`, `temperature=0`, and `max_tokens=200`.

## Features

- Upload note files from your local machine
- Extract and display text from uploaded files
- Split large note content into searchable chunks
- Build a FAISS vector index for semantic retrieval
- Answer questions using OpenAI and your own notes

## Requirements

- Python 3.10+
- `streamlit`
- `PyPDF2`
- `langchain-text-splitters`
- `langchain-openai`
- `langchain-community`
- `python-dotenv`

## Setup

1. Create a virtual environment and activate it.
2. Install dependencies:

```bash
pip install streamlit PyPDF2 langchain-text-splitters langchain-openai langchain-community python-dotenv
```

3. Add your OpenAI API key to a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run

```bash
streamlit run studybot.py
```

## Usage

1. Open the Streamlit app in your browser.
2. Upload a notes file.
3. Wait for the app to extract text and build the semantic index.
4. Type your question into the query field.
5. Review the answer generated from your uploaded notes.

## Notes and limitations

- `.txt` and `.docx` support are listed, but the current extraction code only handles PDF files.
- If `OPENAI_API_KEY` is not set, the app will not be able to generate embeddings or answers.
- The app currently prints raw extracted text and chunk data, which is useful for debugging but may be removed for production.

## Improvements

- Add proper `.txt` and `.docx` extraction support
- Add error handling for missing API keys and invalid uploads
- Cache embeddings so the app does not rebuild them on every query
- Clean up debug output for a more polished user experience
