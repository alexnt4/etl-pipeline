# Modern Data Pipeline: DBT + Airflow + Databricks

A comprehensive data engineering project demonstrating modern data pipeline architecture using DBT Core, Apache Airflow, and Databricks SQL Serverless warehouse.

## 🎯 Project Overview

This project showcases a complete data engineering workflow that:
- Processes TPC-H sample data from Databricks
- Implements data modeling using DBT Core
- Orchestrates pipelines with Apache Airflow
- Leverages Databricks SQL Serverless for computation
- Demonstrates staging, fact tables, and data marts architecture

## 🏗️ Architecture

*[Architecture diagram placeholder - will be added]*

## 📋 Features

### ✅ Completed Implementation
1. **Databricks Configuration** - Catalog and schema setup
2. **DBT Project Configuration** - Complete dbt_project.yml setup
3. **Staging and Source Models** - Raw data ingestion and cleaning
4. **Fact Tables and Data Marts** - Business logic implementation
5. **DBT Macros** - Reusable code components
6. **Generic and Singular Tests** - Data quality validation
7. **Airflow Orchestration** - Automated pipeline execution

### 🔧 Technical Stack
- **Data Warehouse**: Databricks SQL Serverless
- **Data Modeling**: DBT Core
- **Orchestration**: Apache Airflow (Astro Runtime)
- **Data Source**: Databricks TPC-H Sample Dataset
- **Infrastructure**: Docker containers

## 🚀 Getting Started

### Prerequisites

Before running this project, ensure you have:
- [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli) installed
- Docker and Docker Compose running
- Access to a Databricks workspace
- Basic knowledge of SQL and Python

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <https://github.com/alexnt4/etl-pipeline>
   cd dbt-airflow-databricks-pipeline
   ```

2. **Navigate to the project directory**
   ```bash
   cd dbt-dag
   ```

3. **Start the Airflow environment**
   ```bash
   astro dev start
   ```
   This command will:
   - Build the Docker containers
   - Start Airflow webserver, scheduler, and database
   - Install all required dependencies

4. **Access Airflow UI**
   - Open your browser and go to `http://localhost:8080`
   - Default credentials: `admin` / `admin`

### Configuration

#### Databricks Connection Setup

**⚠️ Important**: You must manually configure the Databricks connection in Airflow UI:

1. Go to **Admin** → **Connections**
2. Click **+ Add a new record**
3. Fill in the connection details:
   - **Connection Id**: `databricks_conn`
   - **Connection Type**: `Databricks`
   - **Host**: `https://your-databricks-workspace.cloud.databricks.com`
   - **Extra**: 
     ```json
     {
       "token": "your-databricks-token",
       "http_path": "/sql/1.0/warehouses/your-warehouse-id"
     }
     ```

#### Environment Variables

Create a `.env` file in the project root with:
```bash
DATABRICKS_TOKEN=your_databricks_token
DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/your_warehouse_id
DATABRICKS_CATALOG=your_catalog
DATABRICKS_SCHEMA=your_schema
```

## 📊 Data Pipeline Overview

### Data Flow

The pipeline follows a medallion architecture:

1. **Bronze Layer (Sources)**
   - Raw TPC-H sample data from Databricks
   - Minimal transformations for data ingestion

2. **Silver Layer (Staging)**
   - Data cleaning and standardization
   - Type casting and basic validations
   - Prepared for business logic application

3. **Gold Layer (Facts & Marts)**
   - Business metrics and KPIs
   - Aggregated data for analytics
   - Optimized for reporting and dashboards

### DBT Models Structure

```
models/
├── staging/
│   ├── stg_tpch_orders.sql
│   ├── stg_tpch_line_items.sql
│   └── ...
├── marts/
│   ├── fct_orders.sql
│   ├── int_order_items.sql
│   └── int_order_items_summary.sql
└── sources.yml
```

### Key Transformations

- **Order Processing**: Comprehensive order analysis with line item details
- **Customer Segmentation**: Customer behavior and purchasing patterns
- **Product Performance**: Product sales metrics and trends
- **Supplier Analysis**: Supplier performance and delivery metrics

## 🔍 DBT Features Implemented

### Macros
Custom macros for:
- Common calculations
- Data quality checks
- Reusable transformations

### Testing
- **Generic Tests**: Built-in tests for data validation
- **Singular Tests**: Custom SQL tests for business logic
- **Source Tests**: Validation of raw data quality

### Documentation
- Comprehensive model documentation
- Column descriptions and business logic
- Lineage tracking and dependencies

## 📈 Monitoring and Observability

### Airflow Monitoring
- DAG execution tracking
- Task success/failure notifications
- Performance metrics and logs

### DBT Testing
- Automated data quality checks
- Test results in Airflow UI
- Failure handling and alerting

