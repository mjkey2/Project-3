-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/5DfhLq
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "year" (
    "year" INTEGER   NOT NULL,
    "id" VARCHAR   NOT NULL,
    "quarter" INTEGER   NOT NULL,
    CONSTRAINT "pk_year" PRIMARY KEY (
        "year"
     )
);

CREATE TABLE "wages" (
    "total_wages" INTEGER   NOT NULL,
    "average_weekly_wage" INTEGER   NOT NULL,
    "pct_chg_total_emp" FLOAT   NOT NULL,
    -- LQ means Location Quotient
    "pct_chg_lq_establishments" FLOAT   NOT NULL,
    "pct_chg_lq_total_qtrly_wages" FLOAT   NOT NULL,
    "pct_chg_avg_wkly_wage" FLOAT   NOT NULL,
    CONSTRAINT "pk_wages" PRIMARY KEY (
        "total_wages"
     )
);

CREATE TABLE "area" (
    "area_fips" VARCHAR   NOT NULL,
    "area_title" VARCHAR   NOT NULL,
    "state" VARCHAR   NOT NULL,
    "county" VARCHAR   NOT NULL,
    CONSTRAINT "pk_area" PRIMARY KEY (
        "area_fips"
     )
);

CREATE TABLE "industry" (
    "name" VARCHAR   NOT NULL,
    "area_fips" VARCHAR   NOT NULL,
    "id" VARCHAR   NOT NULL,
    "establishments" INTEGER   NOT NULL,
    "total_employed" INTEGER   NOT NULL,
    "total_wages" INTEGER   NOT NULL,
    "taxable_wage" INTEGER   NOT NULL
);

ALTER TABLE "industry" ADD CONSTRAINT "fk_industry_area_fips" FOREIGN KEY("area_fips")
REFERENCES "area" ("area_fips");

ALTER TABLE "industry" ADD CONSTRAINT "fk_industry_id" FOREIGN KEY("id")
REFERENCES "year" ("id");

ALTER TABLE "industry" ADD CONSTRAINT "fk_industry_total_wages" FOREIGN KEY("total_wages")
REFERENCES "wages" ("total_wages");

