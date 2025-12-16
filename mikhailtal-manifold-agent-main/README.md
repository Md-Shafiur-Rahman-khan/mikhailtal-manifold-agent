# MikhailTal Manifold Agent

An open-source Python trading bot that participates exclusively in Manifold Markets created by **MikhailTal**.

## Features
- Creator-restricted trading
- Edge-based decision making
- Fractional Kelly bet sizing
- Modular, extensible design
- Compatible with manifoldbot ecosystem

## Strategy
The bot estimates true probabilities using conservative regression and trades only when a statistically meaningful edge exists.

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
python scripts/run_bot.py

