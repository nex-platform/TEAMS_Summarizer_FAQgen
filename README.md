# TEAMS Meeting Summarizer & FAQ Generator

A comprehensive Streamlit application that transforms Microsoft Teams meeting transcripts and chat logs into structured, searchable knowledge bases with AI-powered analysis and summarization.

## 🚀 Key Features

### 📥 Input Processing
- **Multiple File Support**: Upload `.docx` or `.txt` files containing meeting transcripts and chat logs
- **Intelligent Merging**: Automatically combines multiple files while preserving chronological order
- **Text Normalization**: Cleans and standardizes text while maintaining technical terminology

### 🤖 AI-Powered Analysis
- **Smart Summarization**: Generates concise, action-oriented meeting summaries using GPT-4o
- **FAQ Extraction**: Automatically identifies and extracts technical Q&A pairs
- **Action Item Detection**: Highlights decisions, action items, and responsible parties
- **Context Preservation**: Maintains important technical details and context

### 📊 Output & Export
- **Structured Documents**: Generates well-formatted Word documents with sections for summary, FAQs, and action items
- **Searchable Knowledge Base**: Creates organized, categorized content for easy reference
- **Custom Templates**: Uses predefined templates for consistent output formatting

### 🔍 Advanced Features
- **Logging System**: Comprehensive logging with different log levels and rotation
- **Error Handling**: Graceful error recovery and user feedback
- **Temporary File Management**: Automatic cleanup of temporary files and images

## 📁 Project Structure

```
TEAMS_Summarizer_FAQgen/
├── backend/               # Core processing logic
│   ├── __init__.py
│   ├── aggregator.py     # Summary and content generation
│   ├── comparators.py    # Text comparison utilities
│   ├── file_io.py        # File handling operations
│   ├── logger.py         # Logging configuration
│   ├── openai_client.py  # OpenAI API integration
│   ├── text_processing.py # Text cleaning and processing
│   └── transcript_merger.py # Transcript merging logic
├── frontend/             # Streamlit UI and presentation
│   ├── app.py            # Main application
│   ├── debug_chunks/     # Debug output storage
│   └── temp_images/      # Temporary image storage
├── docs/                 # Documentation and examples
├── input/                # Sample input files
├── logs/                 # Application logs
│   ├── app.log          # General application logs
│   └── error.log        # Error logs
├── src/                  # Source files
├── .env                 # Environment variables
├── .gitignore           # Git ignore rules
├── README.md            # This file
└── requirements.txt     # Python dependencies
```

## 🛠️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nex-platform/TEAMS_Summarizer_FAQgen.git
   cd TEAMS_Summarizer_FAQgen
   ```

2. **Set up a virtual environment** (recommended)
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

5. **Run the application**
   ```bash
   streamlit run frontend/app.py
   ```

## 📝 Usage

1. Launch the application using the command above
2. Upload your meeting transcript(s) and/or chat log(s)
3. Configure summarization options as needed
4. Click "Generate Summary" to process the documents
5. Review and download the generated documents

## 📊 Logging

The application includes a comprehensive logging system:
- Logs are stored in the `logs/` directory
- `app.log` contains all application logs (INFO level and above)
- `error.log` contains only error messages (ERROR level and above)
- Logs include HTTP status codes for API calls
- Automatic log rotation (5MB per file, 5 backups)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
