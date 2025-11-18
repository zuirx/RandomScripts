from bitcoinlib.wallets import Wallet
import random, requests, sys, datetime

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self): pass

def get_bip39_wordlist():
    url = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()

def get_random_bip39_words(n=12):
    wordlist = get_bip39_wordlist()
    return random.sample(wordlist, n)

if __name__ == "__main__":
    random_words = get_random_bip39_words(12)
    print(" ".join(random_words))


def restore_wallet_from_seed(seed_phrase, wallet_name="restored_wallet"):
    try:
        wallet = Wallet.create(
            wallet_name,
            keys=seed_phrase,
            network='bitcoin',
            witness_type='segwit',
            account_id=0
        )
        
        print(f"Wallet restored successfully!")
        print(f"Wallet name: {wallet_name}")
        print(f"Master public key: {wallet.get_key().wif_public}")
        
        print("\n📊 Address Balances:")
        for key in wallet.keys():
            balance = key.balance()
            if balance > 0:
                print(f"   Address: {key.address}")
                print(f"   Balance: {balance} satoshis")
                print(f"   Balance: {balance / 100000000:.8f} BTC")
        
        return wallet
        
    except Exception as e:
        print(f"Couldn't: {e}")
        return None

if __name__ == "__main__":

    log_file = f"log_{datetime.date.today()}.txt"
    sys.stdout = Logger(log_file)
    sys.stderr = Logger(log_file)

    wallet = 0
    while not wallet:

        random_words = get_random_bip39_words(12)
        seed_phrase = " ".join(random_words)
        wallet = restore_wallet_from_seed(seed_phrase)

    input("WALLET FOUND!")