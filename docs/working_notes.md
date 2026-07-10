# Working Notes

## Current Status

### Documentation
- ✅ Product brief complete
- ✅ MVP scope complete
- ✅ High-level architecture complete
- ✅ User journeys complete
- ✅ Data model complete
- ✅ API design complete
- ✅ ADRs started

### Development Environment
- ✅ Python virtual environment configured
- ✅ Project configured using `pyproject.toml`
- ✅ Dependencies installed
- ✅ `src` package structure established
- ✅ Application installed in editable mode
- ✅ Environment variable management configured (`.env`)

### Backend
- ✅ Minimal FastAPI application running locally
- ✅ Uvicorn development server configured
- ✅ Basic routing implemented
- ✅ Film search endpoint implemented
- ✅ Initial service layer extracted (`film_service.py`)
- ✅ Dedicated TMDB client implemented (`tmdb_client.py`)
- ✅ Successful authenticated requests to the TMDB API
- ✅ Basic separation established between API, service and external client layers

---

## Current Focus

Replace the remaining hard-coded functionality with real TMDB integration and begin introducing automated testing.

---

## Next Steps

1. Integrate `film_service.py` with the TMDB client.
2. Return simplified Culture Engine film data instead of raw TMDB responses.
3. Introduce the first application model (Film / FilmSearchResult).
4. Introduce `pytest` and write the first service-layer tests.
5. Add basic error handling for TMDB requests.
6. Introduce a central configuration module.
7. Review API response models.

---

## Open Questions

- At what point should Docker be introduced?
- When should PostgreSQL replace in-memory data?
- When should routing be split into dedicated router modules?
- When should configuration be centralised into `config.py`?
- How should external API failures be surfaced to the API layer?

---

## Architectural Decisions (Informal)

- Use the `src` project layout.
- Install the project in editable mode during development.
- Keep FastAPI routes thin.
- Keep HTTP concerns within the API layer.
- Keep business logic inside service modules.
- Keep external integrations isolated in dedicated client modules.
- Store secrets outside source control using environment variables.