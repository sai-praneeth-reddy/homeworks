-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/jpxrtq
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


/* 1. Titles */

CREATE TABLE "Titles" (
    "title_id" varchar   NOT NULL,
    "title" varchar   NOT NULL,
    CONSTRAINT "pk_Titles" PRIMARY KEY (
        "title_id"
     )
);




/* 2. Employees Tables */

CREATE TABLE "Employees" (
    "emp_no" int   NOT NULL,
    "emp_title_id" varchar   NOT NULL,
	FOREIGN KEY (emp_title_id) REFERENCES "Titles"(title_id),
    "birth_date" date   NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar   NOT NULL,
    "sex" varchar   NOT NULL,
    "hire_date" date   NOT NULL,
    CONSTRAINT "pk_Employees" PRIMARY KEY (
        "emp_no"
     )
);


/* 3. Salaries Table */

CREATE TABLE "Salaries" (
    "emp_no" int   NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES "Employees"(emp_no),
    "salary" float   NOT NULL,
    CONSTRAINT "pk_Salaries" PRIMARY KEY (
        "emp_no"
     )
);




/* 4. Departments */

CREATE TABLE "Departments" (
    "dept_no" varchar   NOT NULL,
    "dept_name" varchar   NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "dept_no"
     )
);

/* 5. Department Managers */

CREATE TABLE "Department_Managers" (
    "dept_no" varchar   NOT NULL,
	FOREIGN KEY (dept_no) REFERENCES "Departments"(dept_no),
    "emp_no" int   NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES "Employees"(emp_no),
    CONSTRAINT "pk_Department_Managers" PRIMARY KEY (
        "emp_no"
     )
);



/* 6. Department Employees */

CREATE TABLE "Department_Employees" (
    "emp_no" int   NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES "Employees"(emp_no),
    "dept_no" varchar   NOT NULL,
	CONSTRAINT "pk_Department_Employees" PRIMARY KEY (
        "emp_no","dept_no"
     )
);
