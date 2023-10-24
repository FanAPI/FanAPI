import requests

API_BASE_URL = 'https://41c6-77-50-109-213.ngrok-free.app/fanapi'

def generate_api_key(api_key, user_id):
    response = requests.post(f'{API_BASE_URL}/fanapi/generate', headers={'Authorization': api_key}, params={'user_id': user_id})
    return response.json()

def get_api_info(api_key, marker):
    response = requests.get(f'{API_BASE_URL}/fanapi/get_info', params={'api_key': api_key, 'marker': marker})
    return response.json()

def set_balance(api_key, wallet_id, balance):
    data = {'api_key': api_key, 'wallet_id': wallet_id, 'balance': balance}
    response = requests.put(f'{API_BASE_URL}/fanapi/set_balance', json=data)
    return response.json()

def build_transaction(api_key, wallet_id, transaction_amount, password, mode):
    data = {'api_key': api_key, 'wallet_id': wallet_id, 'transaction_amount': transaction_amount, 'password': password, 'mode': mode}
    response = requests.post(f'{API_BASE_URL}/fanapi/build_transaction', json=data)
    return response.json()

def receive_transaction(api_key, check_id, password):
    data = {'api_key': api_key, 'check_id': check_id, 'password': password}
    response = requests.post(f'{API_BASE_URL}/fanapi/receive_transaction', json=data)
    return response.json()

def get_transaction_status(api_key, check_id):
    data = {'api_key': api_key, 'check_id': check_id}
    response = requests.get(f'{API_BASE_URL}/fanapi/transaction_status', params=data)
    return response.json()
