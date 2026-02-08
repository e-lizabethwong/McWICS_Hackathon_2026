-- You can modify the script to suit your needs.

-- If you want to create a new database for Streamlit Apps, run
--CREATE DATABASE STREAMLIT_APPS;
-- If you want to create a specific schema under the database, run
-- CREATE SCHEMA <SCHEMA_NAME>;
-- Or, you can use the PUBLIC schema that was automatically created with the database.

-- If you want all roles to create Streamlit apps in the PUBLIC schema, run
GRANT USAGE ON DATABASE MCWICS_HACKATHON_DATA TO ROLE PUBLIC;
GRANT USAGE ON SCHEMA MCWICS_HACKATHON_DATA.PUBLIC TO ROLE PUBLIC;
--GRANT CREATE STREAMLIT ON SCHEMA STREAMLIT_APPS.PUBLIC TO ROLE PUBLIC;
--GRANT CREATE STAGE ON SCHEMA STREAMLIT_APPS.PUBLIC TO ROLE PUBLIC;

-- Don't forget to grant USAGE on a warehouse.
GRANT USAGE ON WAREHOUSE COMPUTE_WH TO ROLE PUBLIC;

-- If you only want certain roles to create Streamlit apps,
-- or want to enable a different location to store the Streamlit apps,
-- change the database, schema, and role names in the above commands.