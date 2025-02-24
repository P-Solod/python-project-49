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
brain-calc:
	uv run brain-calc
brain-even:
	uv run brain-even
brain-gcd:
	uv run brain-gcd
brain-prime:
	uv run brain-prime
brain-progression:
	uv run brain-progression
