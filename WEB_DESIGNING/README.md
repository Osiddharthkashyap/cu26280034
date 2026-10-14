# Web Designing

Web development laboratory assignments for the Master of Computer Applications
course. The work progresses from HTML structure through CSS, JavaScript, and
server-side PHP/MySQL applications.

## Lab sheets

| Lab sheet | Topics | Contents |
| --- | --- | --- |
| [Lab Sheet 1](lab_sheet_01/) | HTML fundamentals | 25 standalone HTML exercises covering document structure, text formatting, lists, links, images, tables, and forms |
| [Lab Sheet 2](lab_sheet_02/) | CSS | 22 HTML/CSS exercises covering selectors, form styling, layouts, validation, responsive design, and accessibility |
| [Lab Sheet 3](lab_sheet_03/) | JavaScript | 21 exercises covering arithmetic, conditions, loops, arrays, objects, DOM manipulation, validation, events, timers, closures, JSON, ES6 features, sliders, and a to-do list |
| [Lab Sheet 4](lab_sheet_04/) | PHP, Apache, and MySQL | 17 exercises covering local server setup, PHP configuration, database connectivity, CRUD, virtual hosts, authentication, uploads, privileges, sessions, cookies, and CSV export |

## Running the exercises

### HTML, CSS, and JavaScript

Open an `.html` file from `lab_sheet_01`, `lab_sheet_02`, or `lab_sheet_03`
directly in a web browser. Keep the matching `.css` file beside its HTML file
when one is provided. JavaScript exercises run in the browser; use the
developer console to inspect output and errors.

### PHP and MySQL

Lab Sheet 4 requires a local Apache/PHP/MySQL or MariaDB environment. The
repository includes setup notes in:

- [Apache verification](lab_sheet_04/q01_apache_verify/README.md)
- [PHP configuration](lab_sheet_04/q02_php_ini/README.md)
- [MySQL setup](lab_sheet_04/q03_mysql_setup/README.md)
- [Apache virtual hosts](lab_sheet_04/q10_virtual_hosts/README.md)

For the remaining PHP exercises:

1. Copy or serve the `lab_sheet_04` directory from the configured web
   document root.
2. Create the database and credentials described by the setup files before
   running database-dependent exercises.
3. Review [`config/db.php`](lab_sheet_04/config/db.php) and use local
   development credentials only.
4. Open the required PHP file through `http://localhost/...`; do not open PHP
   files with the `file://` protocol.

The individual exercises may create or modify database records, sessions,
cookies, uploaded files, or exported CSV files. Use a test database and
review the source before executing it.
