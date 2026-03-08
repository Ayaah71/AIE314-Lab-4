# LangChain Projects

**Author:** Aya Mamdouh  

This repository contains two advanced LangChain-based applications developed for a MasterClass assignment.  
Both projects demonstrate multi-source retrieval, agent-based reasoning, conversational memory, and structured output generation.

---

## Project 1: Sheglam Makeup Support System

### Overview
A LangChain-based enterprise-style customer support system for Sheglam makeup products.  
It provides step-by-step troubleshooting, warranty information, and advice for products including lipsticks, eyeshadows, and foundations.

### Features
- Document vectorization for product manuals
- Multi-product knowledge base
- Conversation memory for context retention
- Specialized support tools: warranty checker and troubleshooting guide
- Step-by-step recommendations
- Structured and user-friendly responses

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone <(https://github.com/Ayaah71/AIE314-Lab-4)>

2.Navigate to the project folder:

```bash
   cd Sheglam_Support_System
```
3.Install dependencies:
```bash
   pip install -r requirements.txt
```
4.Run the support system:

```bash
python sheglam_support.py
```
Example Usage
Sheglam Makeup Support System
Type 'exit' to stop

User: My lipstick color fades quickly. What should I do?
Support: Apply lip balm, use a lip liner, and reapply every 4 hours.

User: Check the warranty for my foundation.
Support: Warranty valid until 2025. Expiration: 12 months after opening.

User: exit
## Project 2: Academic Research Assistant

### Overview

A LangChain-inspired research assistant capable of retrieving and synthesizing information from Wikipedia and arXiv, generating structured research reports with source citations.

### Features

- Wikipedia and arXiv search integration

- Structured report generation with:

-- Introduction

-- Research findings

-- Conclusion

-- Source citations

- User-friendly interactive interface

- Topic-based filtering for relevance

### Setup Instructions

1.Navigate to the project folder:
```bash
cd Academic_Research_Assistant
```
2.Install dependencies:
```bash
pip install -r requirements.txt
```
3.Run the research assistant:
```bash
python research_assistant.py
```
Example Usage
Academic Research Assistant
Type 'exit' to stop

Research Topic: Egyptian Pharaohs
RESEARCH REPORT

Topic: Egyptian Pharaohs

Introduction:
The pharaohs were the rulers of ancient Egypt from the unification of Upper and Lower Egypt...

Research Findings:
- Paper 1 summary...
- Paper 2 summary...

Conclusion:
Summary of key insights on Egyptian Pharaohs

Sources:
Wikipedia
arXiv

Research Topic: exit
## Repository Structure
LangChain_Projects/
│
├─ Sheglam_Support_System/
│   ├─ sheglam_docs/        # Product manuals (txt files)
│   ├─ sheglam_support.py   # Python code
│   ├─ requirements.txt     # Dependencies
│
├─ Academic_Research_Assistant/
│   ├─ research_assistant.py
│   ├─ requirements.txt     # Dependencies
│
└─ README.md                # This file
## Technologies Used

- Python 3.x

- LangChain & LangChain Community

- ChromaDB (Vector Database)

- HuggingFace Sentence Transformers

- Transformers (Flan-T5 for LLM responses)

- Wikipedia & arXiv APIs

Author

Aya Mamdouh
LangChain project implementations demonstrating retrieval-augmented generation, agent-based systems, and multi-source information management
