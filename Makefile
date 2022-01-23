.PHONY: dev

dev:
	poetry run uvicorn mjw_server.main:app --reload
