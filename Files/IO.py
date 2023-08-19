import json
import nltk
from nltk.tokenize import (wordpunct_tokenize)
import subprocess


# User inputs
db_id = input("Enter the db_id: ")
question = input("Enter the question: ")
question_toks = wordpunct_tokenize(question)
data = [
    {
        "db_id": db_id,
        "question": question,
        "question_toks": question_toks
    }
]


file_path = "/home/husainmalwat/NL-to-SQL-parser/data/spider/dev.json"
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)


shell_file_path = '/home/husainmalwat/NL-to-SQL-parser/scripts/inference/infer_text2sql.sh'
with open('/home/husainmalwat/RESDSQL/null.txt', 'w') as null_file:
    subprocess.run(['sh', shell_file_path], stdout=null_file, stderr=null_file)


file_path = '/home/husainmalwat/NL-to-SQL-parser/predictions/Spider-dev/resdsql_large/pred.sql'
print("----------------------------------------------------------------------------")
with open(file_path, 'r') as file:
    file_contents = file.read()
    print("SQL QUERY: ",file_contents)