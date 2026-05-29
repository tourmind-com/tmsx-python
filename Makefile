# tmsx-python — spec regeneration, tests, sandbox integration harness.
# Driven by .github/workflows/consume-spec.yml; also usable locally.

SPEC         ?= spec/tmsx-hotel-spec.yaml
CASES        ?= spec/tmsx-hotel-cases.yaml
SPEC_VERSION ?= $(shell cat .spec-version 2>/dev/null || echo 0.0.0)
TMSX_BASE_URL ?= http://developers.tourmind.cn

.PHONY: regenerate test integration-test

# Regenerate the typed client from the OpenAPI spec. `--with ruff` puts ruff on
# PATH for the codegen-config.yaml post_hooks (ruff check/format).
regenerate:
	uvx --with ruff --from openapi-python-client openapi-python-client generate \
	  --path $(SPEC) --config codegen-config.yaml --meta none \
	  --overwrite --output-path src/tmsx/_generated
	@echo "$(SPEC_VERSION)" > .spec-version

# Import smoke check + unit tests (exit 5 == pytest collected no tests yet).
test:
	uv run python -c "import tmsx; import tmsx_test_runner; print('import OK')"
	uv run pytest -q || [ $$? -eq 5 ]

# Canonical cross-SDK sandbox harness. Requires TMSX_AGENT_CODE/USERNAME/PASSWORD.
integration-test:
	uv run tmsx-test-runner --all \
	  --cases-file $(CASES) \
	  --agent-code "$(TMSX_AGENT_CODE)" \
	  --username "$(TMSX_USERNAME)" \
	  --password "$(TMSX_PASSWORD)" \
	  --base-url "$(TMSX_BASE_URL)"
