import sqlparse
import json
import os


# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))
current_directory = current_directory[0:-5]


def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        sql_string = ""
        # Using readline()
        line = file.readline()
        while line:
            sql_string += line
            line = file.readline()
    return sql_string

def generate_json_file(db_id):
    dest = current_directory + 'data/spider/'

    sql_file_path = current_directory + f'database/{db_id}/schema.sql'
    sql_string = read_sql_file(sql_file_path)
    sql_lst = sql_string.split('\n')


    tables = []
    cols = []
    col_lst = []
    typ_lst = ["text"]
    pri_keys = []
    fkeys = []
    
    ind = 0

    for i in range(len(sql_lst)):
        try:
            if(sql_lst[i].split()[0]=="CREATE" and sql_lst[i].split()[1] =="TABLE"):
                n = len(sql_lst[i].split()[2])

                table_name = sql_lst[i].split()[-2].replace("\"", "")
                
                tables.append(table_name)
                if(ind!=0):
                    cols.append(col_lst)
                    col_lst = []
                ind+=1
            
            # print(i.split()[0][0])
            if(sql_lst[i].split()[0][0]=="\""):
                col_name = sql_lst[i].split()[0].replace("\"", "")
                typ = sql_lst[i].split()[1].replace("\"", "")
                col_lst.append(col_name)
                typ_lst.append(typ)
            

            if(sql_lst[i].split()[0] == "FOREIGN"):
                fkeylst = []
                ref_table=""
                refkey =""

                x = sql_lst[i].split()[2]
                
                fkey = x.replace("(","").replace(")","").replace("\"","")
                if(fkey!=''):
                    fkeylst.append(fkey)
                
                y = sql_lst[i].split()[4].split('(')
                # print(y)
                ref_table = y[0].replace("(","").replace(")","").replace("\"","")
                refkey = y[1].replace(",","").replace("(","").replace(")","").replace("\"","")

                fcol = 0
                for j in cols:
                    fcol+=len(j)
                for j in col_lst:
                    
                    if(j==fkeylst[0]):
                        break
                    fcol+=1
                fcol+=1
                # fkeys[0].append(fcol)


                rcol = 1
                for j in range(len(tables)):
                    if(tables[j]==ref_table):
                        for m in cols[j]:
                            if(m==refkey):
                                break
                            else:
                                rcol+=1
                        break
                    else:
                        rcol+=len(cols[j])
                # fkeys[1].append(rcol)     
                fkeys.append([fcol, rcol])

    # -----------------------------------------Primary-Keys ----------------------------------------- 
        
            if(sql_lst[i].split()[0] == "PRIMARY"):
                keylst = []
                for x in sql_lst[i].split()[2].split(","):
                    pkey = x.replace("(","").replace(")","").replace("\"","")
                    if(pkey!=''):
                        keylst.append(pkey)
                # pri_keys.append(keylst)
                pcol = 0
                for j in cols:
                    pcol+=len(j)
                for j in col_lst:
                    if(j==keylst[0]):
                        break
                    pcol+=1
                pcol+=1
                pri_keys.append(pcol)
    # ------------------------------------------------------------------------------------------
            
        except:
            pass 
    cols.append(col_lst)
    
    
    
    
    idx = [-1]
    for i in range(len(cols)):
        idx+= ([i]*len(cols[i]))
    
    column_names = ["*"]
    for col in cols:
        column_names+=col

    cols = []
    for i in range(len(idx)):
        cols.append([idx[i], column_names[i]])
    data = {
        
            "column_names": cols,
            "column_names_original": cols,
            "column_types": typ_lst,
            "db_id": db_id,
            "foreign_keys": fkeys,
            "primary_keys": pri_keys,
            "table_names": tables,
            "table_names_original": tables
    }

    file_name = "tables.json" 
    json_list = [data]
    with open(dest + file_name, "w") as file:
        json.dump(json_list, file, indent=4)