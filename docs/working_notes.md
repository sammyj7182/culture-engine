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

### Backend
- ✅ Minimal FastAPI application running locally
- ✅ Uvicorn development server configured
- ✅ Basic routing implemented
- ✅ Film search endpoint implemented
- ✅ Initial service layer extracted (`film_service.py`)
- ✅ Basic separation established between API layer and business logic

---

## Current Focus

Begin replacing the hard-coded film search with a real integration to the TMDB API.

---

## Next Steps

1. Register for a TMDB API key.
2. Introduce environment variable management (`.env`).
3. Build a dedicated TMDB client.
4. Replace hard-coded film search with a real API request.
5. Return structured film results from TMDB.
6. Introduce the first application model for a film.
7. Begin writing tests for the service layer.

---

## Open Questions

- At what point should Docker be introduced?
- When should PostgreSQL replace in-memory data?
- When should routing be split into dedicated router modules?
- What should the long-term project package structure look like?

## Architectural Decisions (Informal)

- Use the `src` project layout.
- Install the project in editable mode during development.
- Keep FastAPI routes thin.
- Keep HTTP concerns within the API layer.
- Keep business logic inside service modules.