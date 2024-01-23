# Project-3

An overview of the project and its purpose
This project uses an ETL workload to create a more manageable datasource for national employment and wages. It includes a dataframe, simple dashboard and an sql database that can be used for additional visualizations and study


To use this project, you will require the python libraries Pandas and Bokeh. We've included the files for a SQL database, and used SQLAlchemy's create_engine function to establish a connection to the database. The data from the SQL table was then exported into a text format using Pandas. The bokeh notebook can be modified to include different visualizations, or tweak the data included in the current ones.


When gathering the data for this project, we required data that was both free, plentiful, and public. The perfect choice was the BLS census, as it met our requirements, and was designed with these projects in mind. Additionally, extra care was taken to ensure that all states were still fairly represented during the cleaning process. 


The primary datasource is located at:
https://data.bls.gov/cew/apps/data_views/data_views.htm#tab=Tables
