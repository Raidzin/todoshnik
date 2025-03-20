# Todoshnik

ToDo service with Litestar, TailwindCSS, HTMX and Hyperscript

## Start todoshnik local

**requirements**

- uv >= 0.6
- node >= 22

### Build tailwindcss

```shell
cd ui
```

```shell
npm install
```

```shell
npm run build
```

### Start litestar

```shell
uv run litestar --app todoshnik:app run
```

then open http://localhost:8000/
