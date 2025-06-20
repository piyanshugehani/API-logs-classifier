# Intelligent Log Classification System

An advanced multi-tiered classification framework designed to automatically categorize system logs using a combination of rule-based, machine learning, and large language model approaches. This system intelligently routes logs through different classification strategies based on pattern complexity and data availability.

## 🏗️ System Architecture

The system employs a three-tier hybrid approach that maximizes classification accuracy while optimizing computational resources:

### Tier 1: Rule-Based Classification (Regex Engine)
- **Purpose**: Handles well-defined, predictable log patterns
- **Mechanism**: Uses compiled regular expressions to match known log formats
- **Advantages**: Ultra-fast processing, deterministic results, zero false positives for known patterns
- **Use Cases**: Standard system events, formatted error messages, timestamp patterns

### Tier 2: Semantic Classification (Transformer + ML)
- **Purpose**: Processes complex patterns with sufficient training data
- **Mechanism**: 
  - Converts logs to semantic embeddings using Sentence Transformers
  - Applies Logistic Regression for final classification
  - Leverages contextual understanding of log content
- **Advantages**: Captures semantic meaning, handles variations in phrasing, scalable
- **Use Cases**: Application-specific logs, error descriptions with context

### Tier 3: Generative Classification (LLM)
- **Purpose**: Handles novel or poorly-labeled complex patterns
- **Mechanism**: Leverages large language models for zero-shot or few-shot classification
- **Advantages**: No training data required, handles previously unseen patterns
- **Use Cases**: New application logs, anomalous events, complex multi-line entries

## Snippets
![image](https://github.com/user-attachments/assets/14d314c2-ce16-48a8-bc77-59d4c3016c0b)
![image](https://github.com/user-attachments/assets/584f32d4-ae92-4d31-8880-98664f6d3457)

### Tier 3: Generative Classification (LLM)
- **Purpose**: Handles novel or poorly-labeled complex patterns
- **Mechanism**: Leverages large language models for zero-shot or few-shot classification
- **Advantages**: No training data required, handles previously unseen patterns
- **Use Cases**: New application logs, anomalous events, complex multi-line entries

## 🧠 How It Works

### Classification Flow
![image](https://github.com/user-attachments/assets/805c74b1-ef42-4ce7-8363-b7e4f63a0c92)

1. **Input Processing**: Raw logs are preprocessed and normalized
2. **Pattern Routing**: System determines the most appropriate classification tier
3. **Hierarchical Classification**: 
   - Regex patterns are tested first (fastest)
   - If no match, semantic analysis is performed
   - Complex cases fallback to LLM processing
4. **Confidence Scoring**: Each classification includes a confidence metric
5. **Output Generation**: Results are compiled with metadata and confidence scores

### Model Training Process
The system uses an iterative training approach:
- **Data Collection**: Logs are collected and manually labeled for training
- **Feature Engineering**: Text preprocessing, tokenization, and embedding generation
- **Model Training**: Logistic regression training on transformer embeddings
- **Validation**: Cross-validation and performance evaluation
- **Model Persistence**: Trained models are serialized for production use

## 📁 Project Structure

```
log-classification-system/
├── training/                    # Model training and regex development
│   ├── train_models.py         # Sentence transformer + logistic regression training
│   ├── regex_patterns.py       # Rule-based pattern definitions
│   └── data_preprocessing.py   # Data cleaning and preparation utilities
├── models/                     # Persisted model artifacts
│   ├── sentence_transformer/   # Pre-trained transformer models
│   ├── logistic_regression.pkl # Trained classification model
│   └── regex_patterns.json     # Compiled regex rules
├── resources/                  # Supporting files and test data
│   ├── test_logs.csv          # Sample log files for testing
│   ├── output_samples/        # Example classification results
│   └── arch.png              # System architecture diagram
├── server.py                  # FastAPI web server implementation
├── classifier.py             # Core classification logic
├── requirements.txt          # Python dependencies
└── README.md                # This documentation
```

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8 or higher
- 4GB+ RAM recommended for transformer models
- Internet connection for initial model downloads

### Installation
1. **Clone and Navigate**:
   ```bash
   git clone <repository-url>
   cd log-classification-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Models** (if not included):
   ```bash
   python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
   ```

### Running the System

**Start the API Server**:
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

## 📊 Usage Examples

### Input Data Format
Your CSV file should contain these columns:
- `source`: Log source identifier (e.g., "web-server", "database")
- `log_message`: The actual log content to be classified

## 🔧 Configuration Options

### Model Configuration
- **Transformer Model**: Configurable sentence transformer model
- **Confidence Thresholds**: Adjustable confidence levels for tier routing
- **Regex Patterns**: Customizable rule-based patterns
- **LLM Settings**: Model selection and prompt engineering

### Performance Tuning
- **Batch Processing**: Configurable batch sizes for bulk classification
- **Caching**: Embedding caching for repeated log patterns
- **Parallel Processing**: Multi-threading for large datasets

## 🎯 Future Enhancements

### LIME Integration (Local Interpretable Model-agnostic Explanations)
Planned implementation of LIME for model explainability:

- **Feature Importance**: Identify which words/phrases influenced classification decisions
- **Local Explanations**: Generate human-readable explanations for individual predictions
- **Model Debugging**: Help identify classification errors and bias
- **Trust Building**: Provide transparency for critical log analysis decisions

*This system is designed to be a comprehensive solution for log classification challenges across various domains and use cases. The hybrid approach ensures both accuracy and efficiency while maintaining flexibility for future enhancements.*
