from bot.trader import Trader

if __name__ == "__main__":
    trader = Trader(use_llm=False)  # Set True to enable LLM
    trader.run()
