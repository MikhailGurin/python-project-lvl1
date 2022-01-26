
install:
	poetry install # создаст виртуальное окружение и установит пакет в него

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build # собрать пакет

publish:
	poetry publish --dry-run # отладка публикации

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall # локальная установка

lint:
	poetry run flake8 brain_games