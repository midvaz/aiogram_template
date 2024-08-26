# Определяем переменную для команды docker-compose и путь к файлу
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
	$(DC) -f $(DC_FILE_PATH) up -d

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

