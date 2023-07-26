import re
import subprocess

def convert(mysql_data):
    sqlite = "-- import to SQLite by running: sqlite3.exe db.sqlite3 -init sqlite.sql\n\n" + \
             "PRAGMA journal_mode = MEMORY;\n" + \
             "PRAGMA synchronous = OFF;\n" + \
             "PRAGMA foreign_keys = OFF;\n" + \
             "PRAGMA ignore_check_constraints = OFF;\n" + \
             "PRAGMA auto_vacuum = NONE;\n" + \
             "PRAGMA secure_delete = OFF;\n" + \
             "BEGIN TRANSACTION;\n\n"

    currentTable = ''

    lines = mysql_data.split('\n')
    skip = [r'^CREATE DATABASE', r'^USE', r'^/\*', r'^--']
    keys = []

    # Used this site to test regexes: https://regex101.com/

    for i in range(len(lines)):
        line = lines[i].strip()
        # Skip lines that match regexes in the skip[] list above
        for regex in skip:
            if re.match(regex, line):
                continue

        # Include all `INSERT` lines. Replace \' by ''
        if re.match(r'^(INSERT|\()', line, re.IGNORECASE):
            sqlite += line.replace(r"\\'", "''") + "\n"
            continue

        # Print the ´CREATE´ line as is and capture the table name
        m = re.match(r"^\s*CREATE TABLE.*[`\"](.*)[`\"]", line, re.IGNORECASE)
        if m:
            currentTable = m.group(1)
            sqlite += "\n" + line + "\n"
            continue

        # Clean table end line like:
        # ) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8 COMMENT='By definition:\r\n- user_group #1 is administrator and will always have all permissions.\r\n- user_group #2 is guest and always have no permissions.\r\n';
        if line.startswith(")"):
            sqlite += ");\n"
            continue

        # Remove CONSTRAINT `fk_address_state1`" part from lines
        line = re.sub(r'^CONSTRAINT [`\'"][\w]+[`\'"][\s]+', '', line, flags=re.IGNORECASE)
        # Replace "XXXXX KEY" by "KEY" except "PRIMARY KEY" "FOREIGN KEY" and "UNIQUE KEY"
        line = re.sub(r'^[^FOREIGN][^PRIMARY][^UNIQUE]\w+\s+KEY', 'KEY', line, flags=re.IGNORECASE)

        # Lines starting with (UNIQUE) KEY are extracted so we declare them all at the end of the script
        # We also append key name with table name to avoid duplicate index name
        # Example: KEY `name` (`permission_name`)
        m = re.match(r'^(UNIQUE\s)*KEY\s+[`\'"](\w+)[`\'"]\s+\([`\'"](\w+)[`\'"]', line, re.IGNORECASE)
        if m:
            keyUnique = m.group(1) if m.group(1) else ""
            keyName = m.group(2)
            colName = m.group(3)
            keys.append(f'CREATE {keyUnique}INDEX `{currentTable}_{keyName}` ON `{currentTable}` (`{colName}`);')
            continue

        # Print all fields definition lines except "KEY" lines and lines starting with ")"
        if not re.match(r'^\)\s*((?![\w]+\sKEY).)*$', line, re.IGNORECASE):
            # Clear invalid keywords
            line = re.sub(r'AUTO_INCREMENT|CHARACTER SET [^ ]+|UNSIGNED', "", line, flags=re.IGNORECASE)
            line = re.sub(r'DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP|COLLATE [^ ]+', "", line, flags=re.IGNORECASE)
            line = re.sub(r"COMMENT\s[\'\"`][^\'\"`]*[\'\"`]", "", line, flags=re.IGNORECASE)  # Corrected line
            line = re.sub(r'SET\([^)]+\)|ENUM[^)]+\)', "TEXT ", line, flags=re.IGNORECASE)
            # Clear weird MySQL types such as varchar(40) and int(11)
            line = re.sub(r'int\([0-9]*\)', "INTEGER", line, flags=re.IGNORECASE)
            line = re.sub(r'varchar\([0-9]*\)|LONGTEXT', "TEXT", line, flags=re.IGNORECASE)

        if line != "":
            sqlite += line + "\n"

    sqlite += "\n"

    # Fix last table line with a comma
    sqlite = sqlite.replace(",\n);", "\n);")

    # Include all gathered keys as CREATE INDEX
    sqlite += "\n\n" + "\n".join(keys) + "\n\n"

    # Re-enable foreign key check
    sqlite += "COMMIT;\n" + \
              "PRAGMA ignore_check_constraints = ON;\n" + \
              "PRAGMA foreign_keys = ON;\n" + \
              "PRAGMA journal_mode = WAL;\n" + \
              "PRAGMA synchronous = NORMAL;\n"

    return sqlite


import re
import subprocess



def convert_mysql_to_sqlite(mysql_dump_file):
    # Read the MySQL dump file
    with open(mysql_dump_file, "r") as file:
        mysql_schema = file.read()

    sqlite_schema = convert(mysql_schema)
    if sqlite_schema:
        # Save the SQLite schema to a new file
        with open('/home/husainmalwat/RESDSQL/data/spider/sample_sqlite.sql', "w") as file:
            file.write(sqlite_schema)

        print("SQLite schema has been saved to sqlite_schema.sql")

mysql_dump_file = "/home/husainmalwat/RESDSQL/data/spider/sample_mysql.sql"
convert_mysql_to_sqlite(mysql_dump_file)