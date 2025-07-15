import os
from datetime import datetime

from airflow import DAG
from cosmos import DbtTaskGroup, ExecutionConfig, ProfileConfig, ProjectConfig
from cosmos.profiles import DatabricksTokenProfileMapping

# Configuración del perfil para Databricks
profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=DatabricksTokenProfileMapping(
        conn_id="databricks_conn",  # ID conexión en Airflow
        profile_args={
            "catalog": "dbt_db",
            "schema": "dbt_schema",
        },
    ),
)

# Configuración del proyecto dbt
project_config = ProjectConfig(
    dbt_project_path="/usr/local/airflow/dags/dbt/dbt_pipeline",  # Ruta a tu proyecto dbt
)

# Configuración de ejecución
execution_config = ExecutionConfig(
    dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",
)

# Definir el DAG
with DAG(
    dag_id="dbt_databricks_dag",
    description="DAG para ejecutar dbt con Databricks usando TaskGroup",
    schedule="@daily",
    start_date=datetime(2025, 7, 14),
    catchup=False,
    tags=["dbt", "databricks", "etl"],
) as dag:
    # Crear el TaskGroup de dbt
    dbt_tg = DbtTaskGroup(
        group_id="dbt_taskgroup",
        project_config=project_config,
        profile_config=profile_config,
        execution_config=execution_config,
        operator_args={
            "install_deps": True,  # Instala dependencias automáticamente
        },
    )
