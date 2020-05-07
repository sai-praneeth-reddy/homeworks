/* 1. List the following details of each employee: employee number, last name, first name, sex, and salary */

select a.emp_no, a.last_name, a.first_name, a.sex, b.salary

	from "Employees" as a
	
		Inner Join
			
		"Salaries" as b
		
	on a.emp_no = b.emp_no;
		
		
/* 2. List first name, last name, and hire date for employees who were hired in 1986 */

select first_name, last_name, hire_date
	
	from "Employees" 
	
	where extract(year from hire_date) = 1986;
	
	
/* 3. List the manager of each department with the following information: department number, department name, 
	the manager's employee number, last name, first name*/
	
select a.dept_no, b.dept_name, a.emp_no, c.last_name, c.first_name

	from "Department_Managers" as a
	
			Inner Join
			
		"Departments" as b
		
	on a.dept_no = b.dept_no
	
			Inner Join
			
		"Employees" as c
			
	on a.emp_no = c.emp_no;


/* 4. List the department of each employee with the following information: employee number, last name, first name, and department name */

select a.emp_no, a.last_name, a.first_name, c.dept_name

	from "Employees" as a
	
			Left Join
		
		"Department_Employees" as b
		
	on a.emp_no = b.emp_no
	
			Left Join
			
		"Departments" as c
		
	on b.dept_no = c.dept_no;


/* 5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B." */

select first_name, last_name, sex
	
	from "Employees"
	
	where first_name = 'Hercules' and last_name like 'B%';


/* 6. List all employees in the Sales department, including their employee number, last name, first name, and department name. */

select a.emp_no, a.last_name, a.first_name, c.dept_name

	from "Employees" as a
	
			Left Join
			
		"Department_Employees" as b
		
	on a.emp_no = b.emp_no
	
			Left Join
			
			"Departments" as c
		
	on b.dept_no = c.dept_no
	
	where dept_name = 'Sales';

/* 7. List all employees in the Sales and Development departments, including their employee number, last name,  first name, 
    and department name. */
	
select a.emp_no, a.last_name, a.first_name, c.dept_name

	from "Employees" as a
	
			Left Join
			
		"Department_Employees" as b
		
	on a.emp_no = b.emp_no
	
			Left Join
			
			"Departments" as c
		
	on b.dept_no = c.dept_no
	
	where dept_name in ('Sales','Development');

/* 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.*/

select last_name, count(*) as Freq

	from "Employees"
	
	group by last_name
	
	order by freq desc;