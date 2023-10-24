###теперь вся информация о платежах сохраняется))



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
api_key = 'ваш_api_ключ'
user_id = 'идентификатор_пользователя'
response = generate_api_key(api_key, user_id)
print(response)
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
api_key = 'ваш_api_ключ'
marker = 'ваш_маркер'
response = get_api_info(api_key, marker)
print(response)
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
api_key = 'ваш_api_ключ'
wallet_id = 'ваш_идентификатор_кошелька'
new_balance = 100.0
response = set_balance(api_key, wallet_id, new_balance)
print(response)
```

#### 4. **Создание транзакции**

- **URL:** `/fanapi/build_transaction`
- **Метод:** `POST`
- **Параметры:** JSON объект с полями:
  - `api_key` (строка, обязательный) - API ключ пользователя.
  - `wallet_id` (строка, обязательный) - Идентификатор кошелька.
  - `transaction_amount` (число, обязательный) - Сумма транзакции.
  - `password` (строка, обязательный) - Пароль для подтверждения транзакции.
  - `mode` (строка, обязательный) - Режим транзакции ("check" для чека или "forward" для прямой транзакции).
- **Возвращаемый результат:** JSON с сообщением о результате операции и идентификатором созданного чека (для режима "check") или информацией о выполненной транзакции (для режима "forward").

Пример использования для режима "check":

```python
api_key = 'ваш_api_ключ'
wallet_id = 'ваш_идентификатор_кошелька'
transaction_amount = 50.0
password = 'ваш_пароль'
mode = 'check'
response = build_transaction(api_key, wallet_id, transaction_amount, password, mode)
print(response)
```

Пример использования для режима "forward":

```python
api_key = 'ваш_api_ключ'
wallet_id = 'идентификатор_кошелька_получателя'
transaction_amount = 50.0
mode = 'forward'
response = build_transaction(api_key, wallet_id, transaction_amount, None, mode)
print(response)
```

#### 5. **Получение статуса транзакции (чека)**

- **URL:** `/fanapi/transaction_status`
- **Метод:** `GET`
- **Параметры:** JSON объект с полями:
  - `api_key` (строка, обязательный) - API ключ пользователя.
  - `check_id` (строка, обязательный) - Идентификатор транзакции (чека).
- **Возвращаемый результат:** JSON с информацией о статусе транзакции (чека), либо сообщение об ошибке.

Пример использования:

```python
api_key = 'ваш_api_ключ'
check_id = 'ваш_идентификатор_чека'
response = get_transaction_status(api_key, check_id)
print(response)
```
