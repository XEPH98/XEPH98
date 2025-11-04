your_project/
├─ pyproject.toml            # build, deps, tools (PEP 621)
├─ README.md                 # what/why/how
├─ LICENSE
├─ .gitignore
├─ .pre-commit-config.yaml   # (optional) auto-format/lint before commits
├─ src/
│  └─ your_package/          # import as `your_package`
│     ├─ __init__.py         # package API surface (exports)
│     ├─ core/               # domain logic (pure, no I/O)
│     │  ├─ __init__.py
│     │  ├─ entities.py      # dataclasses / pydantic models
│     │  ├─ services.py      # use-cases orchestrating entities
│     │  └─ rules.py         # computations/algorithms
│     ├─ adapters/           # “edges”: DB, files, APIs (I/O code)
│     │  ├─ __init__.py
│     │  ├─ repo_file.py     # file-based repository
│     │  └─ repo_sql.py      # SQL repository
│     ├─ interfaces/         # ports/protocols (abstractions)
│     │  └─ repositories.py  # interfaces used by services
│     ├─ cli/                # command-line entrypoints
│     │  └─ main.py
│     ├─ config/             # settings
│     │  ├─ __init__.py
│     │  ├─ schema.py        # Pydantic/BaseSettings or dataclass schema
│     │  └─ defaults.yaml
│     └─ utils/              # small helpers (pure, no project state)
│        └─ io.py
├─ tests/
│  ├─ conftest.py
│  ├─ unit/
│  └─ integration/
├─ scripts/                  # one-off developer scripts (not installed)
│  └─ convert_legacy_data.py
└─ notebooks/                # optional: exploratory work, keep light
