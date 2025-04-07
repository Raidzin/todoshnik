# Todoshnik

ToDo service with Litestar, TailwindCSS, HTMX and Hyperscript

## Start todoshnik local

requirements:

- **uv** >= 0.6
- **node** >= 22
- or **docker**

### Start litestar

```shell
uv run litestar --app todoshnik:app run
```

or

```shell
docker build -t todoshnik .
docker run -p "8000:8000" todoshnik
```

Then open http://localhost:8000/

### Re Build tailwindcss

```shell
cd ui
```

```shell
npm install
```

```shell
npm run build
```
