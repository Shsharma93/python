genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transaction': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Shas'


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = ''
    for key in last_block:
        value = last_block[key]
        hashed_block += str(value)
    print(blockchain)
    print(hashed_block)
    block = {
        'previous_hash': 'XYZ',
        'index': len(blockchain),
        'transaction': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction : ')
    tx_amount = float(input('Please enter transaction amount : '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    return input('Your choice : ')


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 30)


def verify_chain():
    # block_index = 0
    if len(blockchain) > 1:
        for index in range(len(blockchain) - 1):
            if blockchain[index] == blockchain[index + 1][0]:
                return True
            return False
        # for block in blockchain:
        #     block_index += 1
        #     if block == blockchain[block_index][0]:
        #         return True
        #     return False
    return True


waiting_for_input = True

while waiting_for_input:
    print('Please choose the options')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output blockchain blocks')
    print('h: Manipulate the chain')
    print('q or Q: Exit.')
    user_choice = get_user_choice()
    if user_choice == '1':
        recipient, amount = get_transaction_value()
        add_transaction(recipient, amount=amount)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q' or user_choice == 'Q':
        waiting_for_input = False
    else:
        print('Wrong choice')

    # if not verify_chain():
    #     print('Invaid Blockchain')
    #     print(blockchain)
    #     break
else:
    print('User Left')

print('Done!')
