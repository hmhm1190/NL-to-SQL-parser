import json
import nltk
from nltk.tokenize import (wordpunct_tokenize)
import subprocess
import os
import table_json_generator

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))
current_directory = current_directory[0:-5]

# User inputs
db_id = input("Enter the db_id: ")
question = input("Enter the question: ")
question_toks = wordpunct_tokenize(question)

table_json_generator.generate_json_file(db_id)
data = [
    {
        "db_id": db_id,
        "question": question,
        "question_toks": question_toks
    }
]


file_path = current_directory + "data/spider/dev.json"
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)


shell_file_path = current_directory + 'scripts/inference/infer_text2sql.sh'
with open(current_directory + 'null.txt', 'w') as null_file:
    subprocess.run(['sh', shell_file_path], stdout=null_file, stderr=null_file)


file_path = current_directory + 'predictions/Spider-dev/resdsql_large/pred.sql'
print("----------------------------------------------------------------------------")
with open(file_path, 'r') as file:
    file_contents = file.read()
    print("SQL QUERY: ",file_contents)