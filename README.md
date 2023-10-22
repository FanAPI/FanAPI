**Техническая документация API FanAPI**

**Базовый URL API:** `https://41c6-77-50-109-213.ngrok-free.app/fanapi`

### Методы API

#### 1. **Генерация API ключа**

- **URL:** `/fanapi/generate`
- **Метод:** `POST`
- **Параметры:**
  - `api_key` (строка, обязательный) - API ключ пользователя, отправляется в заголовке запроса.
  - `user_id` (строка, обязательный) - Идентификатор пользователя Telegram, отправляется в параметрах запроса.
- **Возвращаемый результат:** JSON с ключом `api_key` и `wallet_id` в случае успешной генерации, либо сообщение об ошибке.

Пример использования:

```python
api_key = 'your_api_key'
user_id = 'user_telegram_id'
response = requests.post(API_BASE_URL + '/generate', headers={'Authorization': api_key}, params={'user_id': user_id})
print(response.json())
```

#### 2. **Получение информации о кошельке**

- **URL:** `/fanapi/get_info`
- **Метод:** `GET`
- **Параметры:**
  - `api_key` (строка, обязательный) - API ключ пользователя.
  - `marker` (строка, обязательный) - Маркер для поиска кошелька.
- **Возвращаемый результат:** JSON с информацией о балансе и идентификаторе кошелька, либо сообщение об ошибке.

Пример использования:

```python
api_key = 'your_api_key'
marker = 'your_marker'
response = requests.get(API_BASE_URL + '/get_info', params={'api_key': api_key, 'marker': marker})
print(response.json())
```

#### 3. **Установка баланса кошелька**

- **URL:** `/fanapi/set_balance`
- **Метод:** `PUT`
- **Параметры:** JSON объект с полями:
  - `api_key` (строка, обязательный) - API ключ пользователя.
  - `wallet_id` (строка, обязательный) - Идентификатор кошелька.
  - `balance` (число, обязательный) - Новый баланс кошелька.
- **Возвращаемый результат:** JSON с сообщением о результате операции.

Пример использования:

```python
api_key = 'your_api_key'
wallet_id = 'your_wallet_id'
new_balance = 100.0
data = {'api_key': api_key, 'wallet_id': wallet_id, 'balance': new_balance}
response = requests.put(API_BASE_URL + '/set_balance', json=data)
print(response.json())
```

#### 4. **Создание транзакции**

- **URL:** `/fanapi/build_transaction`
- **Метод:** `POST`
- **Параметры:** JSON объект с полями:
  - `api_key` (строка, обязательный) - API ключ пользователя.
  - `wallet_id` (строка, обязательный) - Идентификатор кошелька.
  - `transaction_amount` (число, обязательный) - Сумма транзакции.
  - `password` (строка, обязательный) - Пароль для подтверждения транзакции.
- **Возвращаемый результат:** JSON с сообщением о результате операции и идентификатором созданного чека.

Пример использования:

```python
api_key = 'your_api_key'
wallet_id = 'your_wallet_id'
transaction_amount = 50.0
password = 'your_password'
data = {'api_key': api_key, 'wallet_id': wallet_id, 'transaction_amount': transaction_amount, 'password': password}
response = requests.post(API_BASE_URL + '/build_transaction', json=data)
print(response.json())
```

#### 5. **Завершение транзакции**

- **URL:** `/fanapi/receive_transaction`
- **Метод:** `POST`
- **Параметры:** JSON объект с полями:
  - `api_key` (строка, обязательный) - API ключ пользователя.
  - `check_id` (строка, обязательный) - Идентификатор транзакции (чека).
  - `password` (строка, обязательный) - Пароль для подтверждения транзакции.
- **Возвращаемый результат:** JSON с сообщением о результате операции.

Пример использования:

```python
api_key = 'your_api_key'
check_id = 'your_check_id'
password = 'your_password'
data = {'api_key': api_key, 'check_id': check_id, 'password': password}
response = requests.post(API_BASE_URL + '/receive_transaction', json=data)
print(response.json())
```

*Так же ознакомься с FanAPI.py. Там собраны функции для более быстрого обращения к api*
