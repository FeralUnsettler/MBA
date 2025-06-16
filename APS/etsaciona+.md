A seguir vai um **esqueleto de repositório** que reúne:

1. Um **scraper + ETL** que coleta dados da EPTC/Zona Azul (via scraping), normaliza e grava num Data Lake (S3-like) e num Postgres.
2. Uma **API Flask** para expor esses dados.
3. Um **dashboard Streamlit** que consome a API e apresenta KPIs.
4. Tudo containerizado via **Docker** e orquestrado com **docker-compose**.
5. Um **README.md** com documentação para GitHub.

---

## 📁 Estrutura do repositório

```
estaciona_plus/
├── docker-compose.yml
├── README.md
├── postgres/
│   └── init.sql
├── scraper/
│   ├── Dockerfile
│   └── etl.py
├── api/
│   ├── Dockerfile
│   └── app.py
├── dashboard/
│   ├── Dockerfile
│   └── dashboard.py
└── shared/
    └── requirements.txt
```

---

### 1. `shared/requirements.txt`

```txt
Flask==2.2.3
requests==2.28.2
beautifulsoup4==4.11.1
SQLAlchemy==1.4.46
psycopg2-binary==2.9.5
boto3==1.26.64
pandas==1.5.3
streamlit==1.18.1
```

---

### 2. `docker-compose.yml`

```yaml
version: '3.8'
services:
  postgres:
    image: postgres:14-alpine
    volumes:
      - ./postgres/init.sql:/docker-entrypoint-initdb.d/init.sql
    environment:
      POSTGRES_DB: estaciona
      POSTGRES_USER: sa
      POSTGRES_PASSWORD: changeme
    ports:
      - "5432:5432"

  etl:
    build: ./scraper
    depends_on: [postgres]
    environment:
      - DATABASE_URL=postgresql://sa:changeme@postgres:5432/estaciona
      - DATALAKE_PATH=./datalake
    volumes:
      - ./datalake:/app/datalake

  api:
    build: ./api
    depends_on: [postgres]
    environment:
      - DATABASE_URL=postgresql://sa:changeme@postgres:5432/estaciona
    ports:
      - "5000:5000"

  dashboard:
    build: ./dashboard
    depends_on: [api]
    environment:
      - API_URL=http://api:5000
    ports:
      - "8501:8501"
```

---

### 3. `postgres/init.sql`

```sql
CREATE TABLE vagas (
  id SERIAL PRIMARY KEY,
  area VARCHAR(100),
  latitude DOUBLE PRECISION,
  longitude DOUBLE PRECISION,
  status VARCHAR(20),
  coletado_em TIMESTAMP DEFAULT now()
);
```

---

### 4. Scraper + ETL (`scraper/etl.py`)

```python
import os, requests, pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

DB_URL = os.getenv("DATABASE_URL")
DATALAKE = os.getenv("DATALAKE_PATH", "./datalake")
engine = create_engine(DB_URL)

def scrape_zona_azul():
    url = "https://prefeitura.poa.br/.../zona-azul"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    # Exemplo: cada linha de tabela
    rows = []
    for tr in soup.select("table.vagas tr")[1:]:
        cols = [td.get_text(strip=True) for td in tr.find_all("td")]
        rows.append({
            "area": cols[0],
            "latitude": float(cols[1]),
            "longitude": float(cols[2]),
            "status": cols[3]
        })
    return pd.DataFrame(rows)

def save_to_datalake(df, name):
    path = os.path.join(DATALAKE, f"{name}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.parquet")
    df.to_parquet(path, index=False)

def upsert_db(df, table="vagas"):
    df.to_sql(table, con=engine, if_exists="append", index=False)

def main():
    df = scrape_zona_azul()
    save_to_datalake(df, "zona_azul")
    upsert_db(df)

if __name__ == "__main__":
    main()
```

**`scraper/Dockerfile`**

```dockerfile
FROM python:3.10-alpine
WORKDIR /app
COPY ../shared/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY etl.py .
CMD ["python", "etl.py"]
```

---

### 5. API Flask (`api/app.py`)

```python
from flask import Flask, jsonify
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)
engine = create_engine(os.getenv("DATABASE_URL"))

@app.route("/vagas")
def vagas():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM vagas ORDER BY coletado_em DESC LIMIT 100"))
        rows = [dict(r) for r in result]
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

**`api/Dockerfile`**

```dockerfile
FROM python:3.10-alpine
WORKDIR /app
COPY ../shared/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
```

---

### 6. Dashboard Streamlit (`dashboard/dashboard.py`)

```python
import streamlit as st
import requests
import pandas as pd

API_URL = st.secrets.get("API_URL", "http://localhost:5000")

st.title("Estaciona+ Dashboard")
st.markdown("KPIs de vagas em tempo real")

@st.cache_data(ttl=300)
def load_data():
    resp = requests.get(f"{API_URL}/vagas")
    return pd.DataFrame(resp.json())

df = load_data()
st.map(df[['latitude', 'longitude']])
st.dataframe(df)
```

**`dashboard/Dockerfile`**

```dockerfile
FROM python:3.10-alpine
WORKDIR /app
COPY ../shared/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY dashboard.py .
EXPOSE 8501
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

### 7. `README.md`

````md
# Estaciona+

## Visão Geral
Plataforma SaaS para otimização de vagas de Zona Azul em Porto Alegre.

## Como começar

1. Clone este repositório.
2. Ajuste credenciais em `docker-compose.yml`.
3. Rode:
   ```bash
   docker-compose up --build
````

4. Acesse:

   * API: [http://localhost:5000/vagas](http://localhost:5000/vagas)
   * Dashboard: [http://localhost:8501](http://localhost:8501)

## Arquitetura

* **etl**: coleta e grava no PostgreSQL + Data Lake.
* **api**: expõe dados via Flask.
* **dashboard**: consome a API via Streamlit.

## Boas práticas

* Containers isolados e orquestrados.
* Estrutura modular (scraper / api / dashboard).
* Pipeline de ETL automatizado.
* Caching no dashboard para reduzir carga.

```

---

Pronto!  
Este scaffold dá a base para você estender: adicionar outras fontes (EPTC, SigaPay), modelos de ML, CI/CD, testes e monitoramento.
```
