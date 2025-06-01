# CryptoBuddy: Your AI-Powered Crypto Sidekick 🤖🚀

# Predefined crypto dataset
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

# Start the conversation
print("👋 Hey! I’m CryptoBuddy, your AI crypto sidekick! Ask me about trending or sustainable cryptocurrencies.")

def get_user_input():
    return input("\nYou: ").lower()

def get_coin_analysis(coin_name):
    """Analyze a specific cryptocurrency"""
    coin = coin_name.title()  # Capitalize first letter
    if coin not in crypto_db:
        return f"Sorry, I don't have data for {coin}. Try Bitcoin, Ethereum, or Cardano!"
    
    data = crypto_db[coin]
    return f"""
📊 Analysis for {coin}:
• Price Trend: {data['price_trend']} {'📈' if data['price_trend'] == 'rising' else '➡️'}
• Market Cap: {data['market_cap'].upper()} 💰
• Energy Use: {data['energy_use'].upper()} ⚡
• Sustainability Score: {int(data['sustainability_score']*10)}/10 🌱

{'🎯 VERDICT: Strong potential! Price is rising and fundamentals look good.' if data['price_trend'] == 'rising' else '🤔 VERDICT: Watch closely. Current trend is stable.'}
"""

def respond_to_query(query):
    # Check if query matches any coin name first
    for coin in crypto_db.keys():
        if coin.lower() in query.lower():
            print(get_coin_analysis(coin))
            return True
            
    if "sustainable" in query:
        best = max(crypto_db, key=lambda c: crypto_db[c]["sustainability_score"])
        print(f"🌱 CryptoBuddy: Invest in {best}! It’s eco-friendly and has long-term potential.")
    
    elif "trending" in query or "rising" in query:
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        print(f"📈 CryptoBuddy: These cryptos are trending up: {', '.join(trending)}")
    
    elif "long-term" in query or "growth" in query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                print(f"🚀 CryptoBuddy: {name} is trending and sustainable — a solid long-term choice!")
                return
        print("🤔 CryptoBuddy: Hmm...no coin checks all the boxes perfectly, but keep looking!")
    
    elif "energy" in query:
        low_energy = [name for name, data in crypto_db.items() if data["energy_use"] == "low"]
        print(f"🔋 CryptoBuddy: Low-energy cryptos: {', '.join(low_energy)}")
    
    elif "advice" in query or "recommend" in query:
        print("🧠 CryptoBuddy: Think long-term! Look for coins that are both rising and eco-friendly.")
    
    elif "exit" in query or "bye" in query:
        print("👋 CryptoBuddy: See you next time! Remember: Crypto is risky—always do your own research.")
        return False
    
    else:
        print("🤖 CryptoBuddy: Sorry, I didn't get that. Try asking about trends, sustainability, or long-term growth.")
    
    return True

# Chat loop
keep_chatting = True
while keep_chatting:
    query = get_user_input()
    keep_chatting = respond_to_query(query)
