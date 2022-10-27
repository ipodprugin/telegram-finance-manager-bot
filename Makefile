IMAGE_NAME = telegram-finance-bot
CONTAINER_NAME = telegram-finance-bot

all:
	docker build -t $(IMAGE_NAME) .
	docker run -d --name $(CONTAINER_NAME) $(IMAGE_NAME)

del-container:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

restart: del-container all