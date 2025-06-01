# 🧠 **CrytoSideKick**

CrytoSideKick is an AI-powered chatbot that leverages Natural Language Processing (NLP) to help users explore and understand cryptocurrencies. It responds to natural language queries to identify investment insights, trends, and sustainability scores of various coins.

---

## 🚀 **Features**

- 🔍 **Intent Detection**: Understands user queries using NLTK-based NLP.
- 📈 **Market Intelligence**: Responds with details about price trends, sustainability, profitability, and long-term potential.
- 💬 **Crypto Info**: Offers built-in knowledge on Bitcoin, Ethereum, and Cardano.
- 📂 **Logging**: Logs user interactions and errors to `crypto_bot.log`.

---

## 🛠️ **Installation**

### **Requirements**

- Python 3.7+
- `nltk` Python package

### **Setup**

pip install nltk

Then, download the required NLTK data:

import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

### **📄 Logging**
Runtime errors and bot operations are logged in crypto_bot.log.

This helps with debugging and reviewing interaction patterns.

Example log error:

2025-05-29 21:56:25 - ERROR - Error in query interpretation:
Resource punkt_tab not found.

### **▶️ Running the Chatbot**

To start the chatbot, run:

python crypto.py

### **💬 Supported Commands**

help: Show command tips

exit, quit, or bye: Exit the chatbot

