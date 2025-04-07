ARG BASE_LAYER="bookworm-slim"
ARG UV_VERSION="0.6"
ARG PYTHON_VERSION="3.12"

FROM ghcr.io/astral-sh/uv:${UV_VERSION}-python${PYTHON_VERSION}-${BASE_LAYER}

WORKDIR /src

COPY pyproject.toml uv.lock ./

RUN uv sync --compile-bytecode --no-dev

ADD migrations migrations 
ADD ui ui
ADD todoshnik todoshnik

CMD [".venv/bin/python", "-m", "litestar", "--app", "todoshnik:app", "run", "-H", "0.0.0.0"]
