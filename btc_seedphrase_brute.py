from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic
import random, requests, traceback, sys, datetime

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # Required for Python stdout compatibility
        pass



def get_bip39_wordlist():
    """Fetches the official BIP-39 English word list."""
    url = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()

def get_random_bip39_words(n=12):
    """Returns n random words from the BIP-39 English word list."""
    wordlist = get_bip39_wordlist()
    return random.sample(wordlist, n)

if __name__ == "__main__":
    # Example: generate a random 12-word phrase
    random_words = get_random_bip39_words(12)
    print(" ".join(random_words))


def restore_wallet_from_seed(seed_phrase, wallet_name="restored_wallet"):
    """
    Restore a Bitcoin wallet from seed phrase and check balance
    """
    try:
        # Restore wallet from seed phrase
        wallet = Wallet.create(
            wallet_name,
            keys=seed_phrase,
            network='bitcoin',
            witness_type='segwit',  # or 'legacy' or 'p2sh-segwit'
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