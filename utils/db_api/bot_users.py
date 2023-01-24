import requests

from data.config import BACKEND_URL, ADMIN_TOKEN


def create_bot_user(user):
    url = f"{BACKEND_URL}/bot-users/list/"
    # head = {'Authorization': f'Token {ADMIN_TOKEN}'}
    # Add the Authorization header
    head = {'Authorization': f'Token {ADMIN_TOKEN}'}

    body = {
        'telegram_id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }

    res = requests.post(url, headers=head, json=body)
    print(res.text)
