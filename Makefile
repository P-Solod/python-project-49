install:
	uv sync
brain-games:
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/*.whl
reinstall:
	uv tool install --force-reinstall dist/*.whl
lint:
	uv run ruff check brain_games
lint-fix:
	uv run ruff check brain_games --fix
