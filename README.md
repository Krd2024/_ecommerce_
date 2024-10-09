![Python Versions](https://img.shields.io/pypi/pyversions/Django.svg)
# Интернет-магазин (Pet-проект)
## Описание
Данный проект представляет собой интернет-магазин, созданный как pet-проект для демонстрации базовых функций электронной коммерции. После регистрации пользователи могут выполнять различные действия, связанные с выбором товаров и их покупкой.

## Возможности для пользователей:
- Выбор категории товаров: Выберите категорию товаров для просмотра доступных товаров.
- Добавление товаров в корзину: Выберите товары из категории и добавьте их в корзину.
- Просмотр корзины: Посмотрите товары, которые вы добавили в корзину.
- Удаление товаров из корзины: Удаляйте отдельные товары из корзины.
- Очистка корзины: Быстрая очистка всей корзины от товаров.
- Покупка товаров: Совершайте покупку выбранных товаров из корзины.
- Просмотр истории покупок: Просматривайте список ранее купленных товаров.
## Возможности для администратора:
- Добавление товаров: Администраторы могут добавлять новые товары через админ-панель.
- Редактирование товаров: Изменение информации о существующих товарах через админ-панель.
## Админ-панель:
- Для входа в админ-панель используйте следующие учетные данные:

Логин: admin
Пароль: 1

# Технические детали:

## Установка

1.Склонируйте репозиторий:
   ```bash
   git clone https://github.com/Krd2024/_ecommerce_.git.git
```
2.Создание виртуального окружения
```bash
   python -m venv .venv
```
3.Активация виртуального окружения
```bash
   .venv\Scripts\activate
```
4.Установка зависимостей проекта
```bash
   pip install -r requirements.txt
```
**Сгенерировать SECRET_KEY в Django**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
**Сосдать файл .env**
Добавьте соответствующие значения в .env файл:
```python
SECRET_KEY = см. выше
```
5.Запуск
```bash
   python manage.py runserver
```
