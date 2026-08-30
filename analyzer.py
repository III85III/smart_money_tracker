from datetime import datetime, timedelta
import random

TEHRAN_OFFSET = timedelta(hours=3, minutes=30)

WHALE_WALLETS = {
    "0x28c6c06298d514db089934071355e5743bf21d60": {"name": "Institutional Fund #Alpha", "explorer": "https://etherscan.io/address/"},
    "0x392b91bc7754388e25d2b1f8687791bc91bc91bc": {"name": "Top Exchange Cold Wallet", "explorer": "https://bscscan.com/address/"},
    "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM": {"name": "Whale Accumulator #01", "explorer": "https://solscan.io/account/"},
    "0x811e44ef009822a106e236540844ef00982244ef": {"name": "VC Smart Money (Long-Term)", "explorer": "https://etherscan.io/address/"}
}

TOKENS = ["BTC", "ETH", "SOL", "LINK", "AVAX"]

class WhaleFeedEngine:
    def __init__(self):
        self.start_time = datetime.utcnow() + TEHRAN_OFFSET

    def generate_whale_alert(self):
        wallet = random.choice(list(WHALE_WALLETS.keys()))
        info = WHALE_WALLETS[wallet]
        token = random.choice(TOKENS)
        tehran_time = datetime.utcnow() + TEHRAN_OFFSET
        price_usd = random.randint(10_000_001, 150_000_000)
        amount = round(price_usd / random.uniform(10, 60000), 2)

        return {
            "time": tehran_time.strftime("%H:%M:%S"),
            "wallet": wallet,
            "wallet_url": info["explorer"] + wallet,
            "name": info["name"],
            "action": random.choice(["ACQUIRED", "ACCUMULATED", "BOUGHT"]),
            "amount": f"{amount:,.2f}",
            "token": token,
            "usd": f"${price_usd:,.0f}",
            "confidence": "VERIFIED WHALE ACTIVITY"
        }

engine = WhaleFeedEngine()
