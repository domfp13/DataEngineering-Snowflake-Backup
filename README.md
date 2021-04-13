# Snowflake-backup

## Section 1: Database migration tool for Snowflake
Snowflake migration app is meant to be used as a database migration tool for small and medium datasets in Snowflake, using Microservices it creates a container that will run macros in JINJA using DBT (data build tool) in order to get first the DDL and later on the data both will be posted in a AWS S3.
## Section 2: Development Environment Setup
This section will cover the environmental setup for running the code.
### 2.1: Docker-based Environment
This code uses a docker container, you need to fulfill the following
requirements:

 * Have a running docker environment
 * Have `make` installed

### 2.2.- Set-up

```sh
$ cd Snowflake-backup
$ make setup
$ make build
```
