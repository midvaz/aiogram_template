# Определяем переменную для команды docker-compose и путь к файлу

CONFIG_FILE=./.config/config.yaml

postgresql_enabled := $(shell grep "postgresql:" $(CONFIG_FILE) | awk '{print $$2}')
python_enabled := $(shell grep "python:" $(CONFIG_FILE) | awk '{print $$2}')
mongoDB_enabled := $(shell grep "mongoDB:" $(CONFIG_FILE) | awk '{print $$2}')

DC=docker-compose
DC_FILE_PATH=./deploy/docker-compose.yaml

help:
	@echo "Доступные команды:"
	@echo "  up      - Запуск контейнеров в фоновом режиме"
	@echo "  down    - Остановка контейнеров"
	@echo "  build   - Сборка образов"
	@echo "  logs    - Просмотр логов контейнеров"
	@echo "  clean   - Очистка неиспользуемых образов, контейнеров, томов"

# Определяем цель по умолчанию
.DEFAULT_GOAL := help

# # Цели для работы с docker-compose
# .PHONY: up down build logs

# Запуск контейнеров в фоновом режиме
up:
ifeq ($(postgresql_enabled), true)
	@echo "Запуск PostgreSQL..."
	$(DC) -f $(DC_FILE_PATH) up -d postgres
endif
ifeq ($(python_enabled), true)
	@echo "Запуск Python..."
	$(DC) -f $(DC_FILE_PATH) up -d python
endif
ifeq ($(mongoDB_enabled), true)
	@echo "Запуск MongoDB..."
	$(DC) -f $(DC_FILE_PATH) up -d mongo
	$(DC) -f $(DC_FILE_PATH) up -d mongo-express
endif

# Остановка контейнеров
down:
	$(DC) -f $(DC_FILE_PATH) down

# Сборка образов
build:
	$(DC) -f $(DC_FILE_PATH) build

# Просмотр логов контейнеров
logs:
	$(DC) -f $(DC_FILE_PATH) logs -f

# Очистка неиспользуемых образов, контейнеров, томов
clean:
	$(DC) -f $(DC_FILE_PATH) down --volumes --remove-orphans
	docker system prune -f

