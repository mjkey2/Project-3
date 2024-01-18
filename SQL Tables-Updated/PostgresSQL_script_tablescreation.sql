CREATE TABLE CleanData_Table (
    id INTEGER,
    area_code VARCHAR,
    quarter INTEGER,
    year INTEGER,
    establishments INTEGER,
    total_employed INTEGER,
    total_wages NUMERIC,
    taxable_wage NUMERIC,
    average_weekly_wage INTEGER,
    "%chg_lq_estabishments" FLOAT,
    "%chg_total_emp" FLOAT,
    "%chge_lq_total_qtrly_wages" FLOAT,
    "%chge_lq_taxable_wages" FLOAT,
    "%chge_avg_wkly_wage" FLOAT
);

CREATE TABLE LocationInfo (
    area_fips VARCHAR,
    County VARCHAR,
    State VARCHAR
);

CREATE TABLE EstablishmentMetrics (
    id INTEGER PRIMARY KEY,
    establishments INTEGER,
    "%chg_lq_establishments" FLOAT
);

CREATE TABLE EmploymentMetrics (
    id INTEGER PRIMARY KEY,
    total_employed INTEGER,
    "%chg_total_emp" FLOAT
);

CREATE TABLE WageMetrics (
    id INTEGER PRIMARY KEY,
    total_wages NUMERIC,
    taxable_wage NUMERIC,
    average_weekly_wage INTEGER,
    "%chge_lq_total_qtrly_wages" FLOAT,
    "%chge_lq_taxable_wages" FLOAT,
    "%chge_avg_wkly_wage" FLOAT
);

CREATE TABLE QuarterlyChangeMetrics (
    id INTEGER PRIMARY KEY,
    "%chg_lq_estabishments" FLOAT,
    "%chg_total_emp" FLOAT,
    "%chge_lq_total_qtrly_wages" FLOAT,
    "%chge_lq_taxable_wages" FLOAT,
    "%chge_avg_wkly_wage" FLOAT
);