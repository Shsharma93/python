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
    return input('Please enter transaction amount : ')


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
    print('2: Output blockchain blocks')
    print('h: Manipulate the chain')
    print('q or Q: Exit.')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        if tx_amount != '':
            add_transaction(float(tx_amount), get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q' or user_choice == 'Q':
        waiting_for_input = False
    else:
        print('Wrong choice')

    if not verify_chain():
        print('Invaid Blockchain')
        print(blockchain)
        break
else:
    print('User Left')

print('Done!')
