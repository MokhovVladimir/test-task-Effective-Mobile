# Веб-приложение с использованием Nginx и Docker

Минимальный HTTP-сервис на Flask, работающий на Nginx в Docker Compose.

Архитектура проекта построена по принципу reverse proxy:  
- Nginx является единственной точкой входа с хоста и проксирует запросы во внутренний Flask backend.

- Client → Nginx (80) → Flask backend (internal network)

- Backend полностью изолирован от хоста и доступен только внутри Docker-сети.


## Стек технологий

- Python 3.12
- Flask
- Nginx
- Docker
- Docker Compose

## Структура проекта

```text
.
├── .env
├── docker-compose.yml
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── nginx/
│   ├── nginx.conf
│   └── default.conf.template
└── README.md
```

## Конфигурация
Все порты выносятся в .env файл. Пример файла:

```env

PORT_APP=8080
PORT_NGINX=80

```
Описание переменных:

- PORT_APP — порт Flask-приложения внутри Docker-сети

- PORT_NGINX — порт, на котором Nginx доступен с хоста

## Архитектура и принципы
### Backend (Flask)
- Работает внутри Docker-контейнера

- Запускается не от пользователя root

- Порт настраивается через переменные окружения

- Не имеет прямого доступа с хоста (expose, без ports)

- Доступен только через Nginx

### Nginx
- Работает как reverse proxy

- Единственная точка входа с хоста

- Передаёт стандартные заголовки (Host, X-Real-IP, X-Forwarded-For)

- Использует шаблон конфигурации (.template) с подстановкой env-переменных

- Дефолтные конфигурации отключены

- Чистая и минимальная структура конфигов

### Docker Networking
- Используется изолированная bridge-сеть

- Backend не доступен извне Docker

- Взаимодействие сервисов происходит по DNS-именам Docker Compose

### Безопасность
- Backend не проброшен наружу

- Запуск контейнеров без root

- Минимальные базовые образы (python:slim, nginx:alpine)

- Чёткое разделение ответственности сервисов

- Отсутствие хардкода конфигурации

- Добавлен .gitignore для защиты секретов из репозитория

# Запуск проекта
Сборка и запуск сервисов:

```bash

docker-compose up --build
```
После запуска приложение будет доступно по адресу:

```text

http://localhost
```
Ожидаемый ответ:

```text

Hello from Effective Mobile!
```