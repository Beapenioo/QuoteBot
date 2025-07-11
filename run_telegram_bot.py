#!/usr/bin/env python3
"""
Telegram Bot Runner
Bu script telegram bot'u çalıştırır.
"""

import sys
import os

# Proje kök dizinini Python path'ine ekle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.bot.telegram_bot import run_bot

if __name__ == "__main__":
    run_bot() 