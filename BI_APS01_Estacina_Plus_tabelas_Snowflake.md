# Tabela `fato_zona_azul` para o Snowflake conforme o exemplo no PDF e também fornecer um passo a passo com instruções para o deploy no ambiente Snowflake, incluindo como inserir dados e integrar ao seu dashboard.


# Criação da tabela no console Snowflake

1. **Acesse o Snowflake:** Entre na sua conta Snowflake via [https://app.snowflake.com](https://app.snowflake.com) e abra um **Worksheet** (menu *Projects* → *Worksheets* → botão “+” para criar um novo worksheet).

2. **Defina o SQL de criação:** Copie e execute o comando `CREATE TABLE` abaixo no editor SQL do worksheet. Este exemplo cria a tabela `fato_zona_azul` com os campos especificados. Note que em Snowflake `AUTOINCREMENT` (ou `IDENTITY`) só vale para colunas numéricas e gera valores crescentes automaticamente.

   ```sql
   CREATE OR REPLACE TABLE fato_zona_azul (
     id_registro   INTEGER AUTOINCREMENT PRIMARY KEY,
     bairro        VARCHAR,
     data_hora     TIMESTAMP,
     total_vagas   INTEGER,
     ocupadas      INTEGER,
     livres        INTEGER,
     receita       NUMERIC(10,2),
     tarifa_media  NUMERIC(7,2)
   );
   ```

   *Aqui usamos `OR REPLACE` para recriar facilmente se precisar atualizar o esquema. O campo `id_registro` recebe valores sequenciais automaticamente. Em Snowflake, a restrição `PRIMARY KEY` é informativa (não impõe física de unicidade).*

3. **Executar o comando:** Clique em **Run** ou pressione Ctrl+Enter para criar a tabela no warehouse ativo. Caso prefira linha de comando, você pode executar o mesmo SQL via SnowSQL CLI ou usando a API Python (Snowpark/Snowflake Connector).

## Inserir dados (manual ou via script)

* **Inserção manual (SQL):** Pelo console, use comandos `INSERT`. Exemplo de inserção única ou múltipla:

  ```sql
  INSERT INTO fato_zona_azul (bairro,data_hora,total_vagas,ocupadas,livres,receita,tarifa_media) VALUES
    ('Centro', '2025-06-10 08:00:00', 1200, 950, 250, 3800.00, 4.00);
  ```

  Para várias linhas num único comando, separe os valores por vírgula (como exemplificado na documentação).

* **Bulk load (arquivos CSV):** Se tiver um arquivo CSV local, você pode carregar em massa usando um *stage* interno e `COPY INTO`. Exemplo (via Python Connector ou Snowsql):

  ```sql
  -- no Snowflake: define um stage interno apontando para a tabela
  CREATE OR REPLACE TEMPORARY STAGE stg_zona_azul; 
  -- no host local (via SnowSQL ou API Python): envie o CSV para o stage interno da tabela
  PUT file:///path/to/dados.csv @stg_zona_azul;
  -- em seguida, no Snowflake: copie para a tabela
  COPY INTO fato_zona_azul FROM @stg_zona_azul
    FILE_FORMAT = (TYPE = 'CSV' FIELD_DELIMITER = ',' SKIP_HEADER = 1);
  ```

  Como ilustra a documentação, você primeiro executa `PUT` para subir o arquivo e depois `COPY INTO`.

* **Inserção via Python:** Use o conector Snowflake para Python ou Snowpark para executar inserts. Por exemplo, com o Snowflake Connector:

  ```python
  import snowflake.connector
  # conecta ao Snowflake
  conn = snowflake.connector.connect(
      user='SEU_USUARIO', password='SUA_SENHA',
      account='seu-acc', warehouse='WH_ETL',
      database='DB_POC', schema='PUBLIC'
  )
  cur = conn.cursor()
  # exemplo de INSERT (com placeholders)
  cur.execute(
      "INSERT INTO fato_zona_azul(bairro,data_hora,total_vagas,ocupadas,livres,receita,tarifa_media) "
      "VALUES (%s, %s, %s, %s, %s, %s, %s)",
      ('Centro', '2025-06-10 08:00:00', 1200, 950, 250, 3800.00, 4.00)
  )
  conn.commit()
  ```

  Ou usando Snowpark Python:

  ```python
  from snowflake.snowpark import Session
  # parâmetros de conexão em dicionário (pode vir de snowflake.connector.connect ou do arquivos de configuração)
  conn_params = {
      "account": "seu-acc",
      "user": "SEU_USUARIO",
      "password": "SUA_SENHA",
      "warehouse": "WH_ETL",
      "database": "DB_POC",
      "schema": "PUBLIC"
  }
  session = Session.builder.configs(conn_params).create()
  # Inserir via SQL Snowpark
  session.sql("""
    INSERT INTO fato_zona_azul (bairro,data_hora,total_vagas,ocupadas,livres,receita,tarifa_media)
    VALUES ('Centro','2025-06-10 08:00:00',1200,950,250,3800.00,4.00)
  """).collect()
  # Ou criando um DataFrame e salvando
  data = [("Centro","2025-06-10 08:00:00",1200,950,250,3800.00,4.00)]
  df = session.create_dataframe(data, schema=["bairro","data_hora","total_vagas","ocupadas","livres","receita","tarifa_media"])
  df.write.save_as_table("fato_zona_azul", mode="append")
  ```

  *Observação:* Ao usar dataframes para inserir, omita a coluna de auto-incremento; Snowflake preencherá `id_registro` automaticamente.

## Conexão Snowflake a partir de um app Streamlit

1. **Dependências:** No ambiente Python da app Streamlit, instale:

   ```
   pip install streamlit snowflake-snowpark-python snowflake-connector-python
   ```

2. **Configurar segredos:** No diretório da app, crie (por exemplo) `.streamlit/secrets.toml` com credenciais Snowflake:

   ```toml
   [snowflake]
   account = "seu-acc"
   user = "SEU_USUARIO"
   password = "SUA_SENHA"
   role = "public"
   warehouse = "WH_ETL"
   database = "DB_POC"
   schema = "PUBLIC"
   ```

   O Streamlit buscará essas configurações automaticamente.

3. **Código de conexão:** Use a API integrada `st.connection("snowflake")` do Streamlit para obter um objeto de conexão. Em seguida, use `.query()` para executar SQL. Exemplo no seu script `streamlit_app.py`:

   ```python
   import streamlit as st

   conn = st.connection("snowflake")  # cria SnowflakeConnection usando as credenciais em secrets
   df = conn.query("SELECT * FROM fato_zona_azul")  # retorna um DataFrame pandas
   for row in df.itertuples():
       st.write(row)  # exibe resultado na app
   ```

   O método `.query()` do SnowflakeConnection cuida de caching e *retry* de consultas. (Exemplos completos do uso de `st.connection` podem ser vistos na \[doc Streamlit].)

4. **Snowpark no Streamlit (opcional):** O objeto `SnowflakeConnection` do Streamlit também permite usar Snowpark (ver \[18] "Use a Snowpark session"), mas para a maioria das consultas simples `.query()` e o conector Python são suficientes.

## Permissões no Snowflake (leitura e escrita)

Para que seu app (ou ETL) acesse a tabela, o usuário/SnowflakeRole deve ter privilégios adequados:

* **Criar um Role dedicado:** Exemplo:

  ```sql
  CREATE ROLE app_role;
  GRANT ROLE app_role TO USER seu_user;
  USE ROLE SECURITYADMIN;
  GRANT USAGE ON WAREHOUSE WH_ETL TO ROLE app_role;
  GRANT USAGE ON DATABASE DB_POC TO ROLE app_role;
  GRANT USAGE ON SCHEMA DB_POC.PUBLIC TO ROLE app_role;
  GRANT SELECT, INSERT ON ALL TABLES IN SCHEMA DB_POC.PUBLIC TO ROLE app_role;
  ```

  *Observação:* ao conceder privilégios em objetos de esquema, o papel também precisa ter `USAGE` no banco e schema pai. No exemplo acima, `app_role` pode agora ler e inserir em qualquer tabela no schema (incluindo `fato_zona_azul`).

* **Permissões mínimas:** Alternativamente, conceda diretamente na tabela:

  ```sql
  GRANT SELECT, INSERT ON TABLE DB_POC.PUBLIC.fato_zona_azul TO ROLE app_role;
  ```

  (Isso assume que `app_role` já tem `USAGE` em DB e schema.) Esses comandos seguem a sintaxe do Snowflake.

* **Uso no app:** No Streamlit, especifique o `role = "app_role"` nas credenciais para que o aplicativo herde esses privilégios.

## Automatizar ingestão de dados (ETL/CSV/Snowpipe)

Para cargas automáticas futuras, você pode usar:

* **Snowpipe:** O Snowpipe é uma ferramenta Snowflake para ingestão contínua. Você cria um *pipe* que contém um comando `COPY INTO` apontando para um stage (interno ou externo). O Snowpipe monitora novos arquivos e carrega automaticamente em micro-lotes. Exemplo:

  ```sql
  CREATE OR REPLACE PIPE pipe_zona_azul AS
    COPY INTO fato_zona_azul
    FROM @mystage/zona_azul
    FILE_FORMAT = (TYPE = 'CSV' FIELD_DELIMITER = ',' SKIP_HEADER = 1)
    ON_ERROR = 'CONTINUE';
  ```

  Depois, configure notificações (SQS, Pub/Sub, etc) ou auto-ingest para que, ao enviar um CSV para `@mystage/zona_azul`, o Snowpipe carregue os dados automaticamente. Isso torna o dado disponível em minutos.

* **Carga manual agendada:** Você pode agendar tarefas para executar `COPY` periodicamente. Por exemplo, pelo Python Connector:

  ```python
  cur.execute("PUT file:///tmp/novos_dados.csv @%fato_zona_azul") 
  cur.execute("COPY INTO fato_zona_azul")
  ```

  A documentação mostra um exemplo semelhante para carregar vários arquivos locais.

* **Write\_pandas (Snowpark):** Para inserir DataFrames pandas diretamente, use `session.write_pandas(df, "fato_zona_azul")`. Essa função escreve um pandas DataFrame na tabela especificada. Por exemplo:

  ```python
  import pandas as pd
  from snowflake.snowpark import Session
  from snowflake.snowpark.pandas import write_pandas

  session = Session.builder.configs(conn_params).create()
  pdf = pd.DataFrame({...})  # dados pandas
  write_pandas(session._conn, pdf, 'FATO_ZONA_AZUL')  # insere dados
  ```

  (No Snowpark 1.x, use `session.write_pandas(pdf, "fato_zona_azul")` diretamente.)

* **Ferramentas ETL:** Você também pode usar ferramentas de integração (Airflow, Matillion, Fivetran etc.) ou a API do Snowflake em Python/Java para automatizar fluxos de dados.

**Resumindo:** cadastre um stage (interno ou externo), crie um pipe/Snowpipe ou tarefas agendadas para copiar CSVs, e use `COPY INTO` ou o utilitário `write_pandas`. Isso permite que seus dados sejam carregados automaticamente no futuro.

Cada passo acima pode ser adaptado à sua infraestrutura (ex.: buckets S3, Azure Blob, APIs de coleta etc.), mas os comandos SQL e exemplos de código apresentados já fornecem a base completa para criar, popular e consultar a tabela `fato_zona_azul` no Snowflake.

**Referências:** documentação oficial Snowflake para criação de tabelas e colunas com `AUTOINCREMENT`, uso do conector Python, Snowpark e pandas, permissões de acesso e Snowpipe para ingestão contínua.
