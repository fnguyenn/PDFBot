OCR_UTILS.py
Python Image Library (PIL), imports Image, which allows me to open and manipulate image files

    Pytesseract is Python Wrapper for Google's Tesseract-OCR engine. It allows Python to interact with Tesseract for extracting text from images

    Fitz is from the PyMuPDF library. This library enables reading and manipulating PDF files, including rendering pages as images.

    OS is Python’s built-in os library to handle file paths and directory creation.

    Shutil library, which is used here for deleting directories and their contents.

LANGCHAIN_PIPELINE.PY
RunnablePassthrough is a utility that passes inputs directly through—used in chaining steps when no transformation is needed.

    StrOutputParser is a parser  that converts the language model’s output to a plain string.

    RecursiveCharacterTextSplitter is a text splitter that recursively splits long text into smaller chunks while preserving semantic boundaries.

    FAISS is a vector store integration from LangChain. FAISS is a library for efficient similarity search on vector embeddings.

    OpenAIEmbeddings is the class for generating text embeddings using OpenAI models.

    ChatOpenAI imports the chat model interface to access OpenAI’s GPT models via LangChain.

    PromptTemplate is LangChain's way of formatting and filling prompts for language models.
