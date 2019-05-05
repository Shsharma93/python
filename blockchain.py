blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return float(input('Please enter transaction amount : '))


def get_user_choice():
    return input('Your choice : ')


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)

def verify_chain():
    for block in blockchain:
        

while True:
    print('Please choose the options')
    print('1: Add a new transaction value')
    print('2: Output blockchain blocks')
    print('h: Manipulate the chain')
    print('q or Q: Exit.')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
        print(blockchain)
    elif user_choice == 'q' or user_choice == 'Q':
        break
    else:
        print('Wrong choice')


print('Done!')
