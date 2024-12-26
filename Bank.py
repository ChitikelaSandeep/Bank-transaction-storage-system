import hashlib
import datetime
import json


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash for this block.
        """
        block_string = f"{self.index}{self.timestamp}{json.dumps(self.data)}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


def create_genesis_block():
    """
    Create the first block in the blockchain, called the Genesis Block.
    """
    return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")


class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]

    def get_latest_block(self):
        """
        Get the last block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Add a new block to the blockchain with the provided data.
        """
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), str(datetime.datetime.now()), data, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Verify if the blockchain is valid by checking hashes and links.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate the current block's hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate the previous block's hash link
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


def main():
    """
    Main CLI for interacting with the blockchain system.
    """
    print("Welcome to the Blockchain Bank Record System!")
    bank_chain = Blockchain()

    while True:
        print("\nOptions:")
        print("1. Add a Transaction")
        print("2. View Blockchain")
        print("3. Validate Blockchain")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user = input("Enter user name: ")
            transaction_type = input("Enter transaction type (Deposit/Withdraw): ")
            amount = input("Enter amount: ")

            data = {
                "user": user,
                "transaction_type": transaction_type,
                "amount": amount
            }

            bank_chain.add_block(data)
            print("Transaction added to the blockchain!")

        elif choice == "2":
            print("\nBlockchain Records:")
            for block in bank_chain.chain:
                print(f"\nIndex: {block.index}")
                print(f"Timestamp: {block.timestamp}")
                print(f"Data: {block.data}")
                print(f"Hash: {block.hash}")
                print(f"Previous Hash: {block.previous_hash}")

        elif choice == "3":
            if bank_chain.is_chain_valid():
                print("Blockchain is valid!")
            else:
                print("Blockchain is invalid!")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")


# Entry point for the script
if __name__ == "__main__":
    main()
