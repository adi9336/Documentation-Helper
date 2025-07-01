# LangChain Documentation Helper

A Streamlit-based chatbot that helps users navigate and understand LangChain documentation by providing intelligent answers to questions using RAG (Retrieval-Augmented Generation) with Pinecone vector database.

## 🚀 Features

- **Intelligent Q&A**: Ask questions about LangChain documentation and get accurate answers
- **Source Citations**: Each answer includes links to the relevant documentation sources
- **Chat Interface**: Interactive chat-like interface built with Streamlit
- **Vector Search**: Uses Pinecone vector database for efficient document retrieval
- **OpenAI Integration**: Powered by OpenAI's GPT models for natural language understanding

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, LangChain
- **Vector Database**: Pinecone
- **LLM**: OpenAI GPT
- **Document Processing**: BeautifulSoup4, LangChain document loaders

## 📋 Prerequisites

Before running this project, you'll need:

1. **Python 3.11+** installed on your system
2. **OpenAI API Key** - Get one from [OpenAI Platform](https://platform.openai.com/)
3. **Pinecone API Key** - Get one from [Pinecone Console](https://app.pinecone.io/)
4. **Pinecone Environment** - Your Pinecone environment (e.g., `us-east-1-aws`)

## 🚀 Installation

### Option 1: Using pip (Recommended)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd documentation-helper
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Using pipenv

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd documentation-helper
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   pipenv shell
   ```

## ⚙️ Configuration

1. **Create environment file**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   PINECONE_ENVIRONMENT=your_pinecone_environment_here
   ```

2. **Set up Pinecone Index**
   - Create a new index in your Pinecone console
   - Use dimension: `1536` (for text-embedding-3-small)
   - Use metric: `cosine`

## 📚 Data Ingestion

Before using the chatbot, you need to ingest the LangChain documentation:

1. **Download documentation** (if not already present)
   ```bash
   # The ingestion script will download LangChain docs automatically
   ```

2. **Run the ingestion script**
   ```bash
   python ingestion.py
   ```
   
   This will:
   - Download LangChain documentation
   - Process and chunk the documents
   - Upload embeddings to Pinecone
   - Create the vector index

## 🎯 Usage

1. **Start the Streamlit app**
   ```bash
   streamlit run main.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:8501`

3. **Ask questions**
   - Type your question about LangChain in the input field
   - Press Enter or click the button
   - Get answers with source citations

## 📁 Project Structure

```
documentation-helper/
├── backend/
│   ├── __init__.py
│   └── core.py              # Main LLM logic and RAG implementation
├── langchain-docs/          # Downloaded documentation (gitignored)
├── venv/                    # Virtual environment (gitignored)
├── .env                     # Environment variables (gitignored)
├── .gitignore              # Git ignore rules
├── LICENSE                 # Apache 2.0 license
├── Pipfile                 # Dependencies (pipenv)
├── Pipfile.lock            # Locked dependencies
├── requirements.txt        # Dependencies (pip)
├── README.md              # This file
├── ingestion.py           # Data ingestion script
└── main.py                # Streamlit application
```

## 🔧 Key Components

### `main.py`
- Streamlit web interface
- Chat history management
- User interaction handling

### `backend/core.py`
- RAG implementation using LangChain
- Pinecone vector store integration
- OpenAI LLM configuration

### `ingestion.py`
- Document downloading and processing
- Text chunking and embedding
- Vector database population

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the amazing framework
- [OpenAI](https://openai.com/) for the language models
- [Pinecone](https://pinecone.io/) for the vector database
- [Streamlit](https://streamlit.io/) for the web framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/documentation-helper/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

---

**Happy coding! 🚀**