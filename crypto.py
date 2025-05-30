
# Adding NLP Functionality

import nltk
import logging
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from typing import List, Dict, Any
import sys

# Configuring logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('crypto_bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
except Exception as e:
    logging.error(f"Failed to download NLTK data: {e}")
    sys.exit(1)

# Setup NLP tools
lemmatizer = WordNetLemmatizer()

class CryptoBot:
    def __init__(self):
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3,
                "description": "The first and most well-known cryptocurrency"
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6,
                "description": "A platform for decentralized applications"
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8,
                "description": "A proof-of-stake blockchain platform"
            }
        }
        self.intents = {
            "sustainability": ["eco", "green", "sustainable", "environment", "low", "energy"],
            "trending": ["trend", "rising", "up", "increase"],
            "long_term": ["long", "future", "growth", "hold", "potential"],
            "profitability": ["profit", "invest", "buy", "high", "market", "return"],
            "info": ["what", "tell", "about", "information", "details"]
        }

    def greet_user(self) -> None:
        """Display welcome message to the user."""
        print("Hey there! I'm CryptoBuddy: your AI-powered financial sidekick!")
        print("Ask me about trending, sustainable, or profitable cryptocurrencies! ")
        print("Type 'help' for available commands or 'exit' to quit.")

    def interpret_query(self, user_query: str) -> List[str]:
        """
        Analyze user query to detect intents using NLP.
        
        Args:
            user_query (str): The user's input query
            
        Returns:
            List[str]: List of detected intents
        """
        try:
            tokens = word_tokenize(user_query.lower())
            lemmas = [lemmatizer.lemmatize(token) for token in tokens]
            
            detected = []
            for intent, keywords in self.intents.items():
                if any(lemma in keywords for lemma in lemmas):
                    detected.append(intent)
            
            return detected
        except Exception as e:
            logging.error(f"Error in query interpretation: {e}")
            return []

    def get_response_nlp(self, user_query: str) -> None:
        """
        Generate appropriate response based on detected intents.
        
        Args:
            user_query (str): The user's input query
        """
        try:
            detected_intents = self.interpret_query(user_query)

            if not detected_intents:
                print("I'm not sure what you meant. Try asking about trends, sustainability, or profits.")
                print("Type 'help' for available commands.")
                return

            if "info" in detected_intents:
                self._handle_info_query(user_query)
                return

            if "sustainability" in detected_intents:
                self._handle_sustainability_query()

            if "trending" in detected_intents:
                self._handle_trending_query()

            if "long_term" in detected_intents:
                self._handle_long_term_query()

            if "profitability" in detected_intents:
                self._handle_profitability_query()

        except Exception as e:
            logging.error(f"Error generating response: {e}")
            print("Sorry, I encountered an error. Please try again.")

    def _handle_info_query(self, query: str) -> None:
        """Handling queries requesting information about specific cryptocurrencies."""
        for coin in self.crypto_db:
            if coin.lower() in query.lower():
                data = self.crypto_db[coin]
                print(f"\n{coin} Information:")
                print(f"Description: {data['description']}")
                print(f"Price Trend: {data['price_trend']}")
                print(f"Market Cap: {data['market_cap']}")
                print(f"Sustainability Score: {data['sustainability_score']}/10")
                return
        print("I don't have information about that cryptocurrency. Try Bitcoin, Ethereum, or Cardano.")

    def _handle_sustainability_query(self) -> None:
        """Handle queries about cryptocurrency sustainability."""
        recommend = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
        print(f"{recommend} is highly sustainable and eco-friendly! Great for green investing.")
        print(f"Sustainability Score: {self.crypto_db[recommend]['sustainability_score']}/10")

    def _handle_trending_query(self) -> None:
        """Handle queries about trending cryptocurrencies."""
        trending = [coin for coin, data in self.crypto_db.items() if data["price_trend"] == "rising"]
        if trending:
            print("These cryptos are currently trending up:")
            for coin in trending:
                print(f" - {coin}")
        else:
            print("No cryptocurrencies are currently trending up.")

    def _handle_long_term_query(self) -> None:
        """Handle queries about long-term investment potential."""
        long_term = [coin for coin, data in self.crypto_db.items() 
                    if data["price_trend"] == "rising" and data["sustainability_score"] > 6]
        if long_term:
            for coin in long_term:
                print(f"{coin} is rising and sustainable – ideal for long-term growth!")
        else:
            print("No cryptocurrencies currently meet the criteria for long-term investment.")

    def _handle_profitability_query(self) -> None:
        """Handle queries about profitable investment opportunities."""
        profitable = [coin for coin, data in self.crypto_db.items() 
                     if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if profitable:
            for coin in profitable:
                print(f"Consider investing in {coin} — it's both profitable and growing!")
        else:
            print("No cryptocurrencies currently meet the criteria for profitable investment.")

    def run(self) -> None:
        """Main loop to run the chatbot."""
        self.greet_user()
        while True:
            try:
                user_query = input("\nYou: ").strip()
                
                if not user_query:
                    continue
                    
                if user_query.lower() in ["exit", "quit", "bye"]:
                    print("Bye! Stay smart, stay sustainable. ")
                    break
                    
                if user_query.lower() == "help":
                    print("\nAvailable commands:")
                    print("- Ask about sustainability")
                    print("- Ask about trending cryptocurrencies")
                    print("- Ask about long-term investments")
                    print("- Ask about profitable opportunities")
                    print("- Ask for information about specific cryptocurrencies")
                    print("- Type 'exit' to quit")
                    continue
                    
                self.get_response_nlp(user_query)
                
            except KeyboardInterrupt:
                print("\nGoodbye! Thanks for chatting!")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                print("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    bot = CryptoBot()
    bot.run()
