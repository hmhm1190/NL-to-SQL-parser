lst = [
         [
            -1,
            "*"
         ],
         [
            0,
            "agent code"
         ],
         [
            0,
            "agent name"
         ],
         [
            0,
            "working area"
         ],
         [
            0,
            "commission"
         ],
         [
            0,
            "phone no"
         ],
         [
            0,
            "country"
         ],
         [
            1,
            "cust code"
         ],
         [
            1,
            "cust name"
         ],
         [
            1,
            "cust city"
         ],
         [
            1,
            "working area"
         ],
         [
            1,
            "cust country"
         ],
         [
            1,
            "grade"
         ],
         [
            1,
            "opening amt"
         ],
         [
            1,
            "receive amt"
         ],
         [
            1,
            "payment amt"
         ],
         [
            1,
            "outstanding amt"
         ],
         [
            1,
            "phone no"
         ],
         [
            1,
            "agent code"
         ],
         [
            2,
            "ord num"
         ],
         [
            2,
            "ord amount"
         ],
         [
            2,
            "advance amount"
         ],
         [
            2,
            "ord date"
         ],
         [
            2,
            "cust code"
         ],
         [
            2,
            "agent code"
         ],
         [
            2,
            "ord description"
         ]
      ]
lst_fin = []
for i in lst:
    lst_fin.append(i[1])
print(lst_fin)

element = 'ord num'


indexes = []
for i in range(len(lst_fin)):
    if lst_fin[i] == element:
        indexes.append(i)

print(indexes)

'''
{
      "column_names": [
         [
            -1,
            "*"
         ],
         [
            0,
            "agent code"
         ],
         [
            0,
            "agent name"
         ],
         [
            0,
            "working area"
         ],
         [
            0,
            "commission"
         ],
         [
            0,
            "phone no"
         ],
         [
            0,
            "country"
         ],
         [
            1,
            "cust code"
         ],
         [
            1,
            "cust name"
         ],
         [
            1,
            "cust city"
         ],
         [
            1,
            "working area"
         ],
         [
            1,
            "cust country"
         ],
         [
            1,
            "grade"
         ],
         [
            1,
            "opening amt"
         ],
         [
            1,
            "receive amt"
         ],
         [
            1,
            "payment amt"
         ],
         [
            1,
            "outstanding amt"
         ],
         [
            1,
            "phone no"
         ],
         [
            1,
            "agent code"
         ],
         [
            2,
            "ord num"
         ],
         [
            2,
            "ord amount"
         ],
         [
            2,
            "advance amount"
         ],
         [
            2,
            "ord date"
         ],
         [
            2,
            "cust code"
         ],
         [
            2,
            "agent code"
         ],
         [
            2,
            "ord description"
         ]
      ],
      "column_names_original": [
         [
            -1,
            "*"
         ],
         [
            0,
            "AGENT_CODE"
         ],
         [
            0,
            "AGENT_NAME"
         ],
         [
            0,
            "WORKING_AREA"
         ],
         [
            0,
            "COMMISSION"
         ],
         [
            0,
            "PHONE_NO"
         ],
         [
            0,
            "COUNTRY"
         ],
         [
            1,
            "CUST_CODE"
         ],
         [
            1,
            "CUST_NAME"
         ],
         [
            1,
            "CUST_CITY"
         ],
         [
            1,
            "WORKING_AREA"
         ],
         [
            1,
            "CUST_COUNTRY"
         ],
         [
            1,
            "GRADE"
         ],
         [
            1,
            "OPENING_AMT"
         ],
         [
            1,
            "RECEIVE_AMT"
         ],
         [
            1,
            "PAYMENT_AMT"
         ],
         [
            1,
            "OUTSTANDING_AMT"
         ],
         [
            1,
            "PHONE_NO"
         ],
         [
            1,
            "AGENT_CODE"
         ],
         [
            2,
            "ORD_NUM"
         ],
         [
            2,
            "ORD_AMOUNT"
         ],
         [
            2,
            "ADVANCE_AMOUNT"
         ],
         [
            2,
            "ORD_DATE"
         ],
         [
            2,
            "CUST_CODE"
         ],
         [
            2,
            "AGENT_CODE"
         ],
         [
            2,
            "ORD_DESCRIPTION"
         ]
      ],
      "column_types": [
         "char",
         "char",
         "char",
         "number",
         "char",
         "char",
         "varchar2",
         "varchar2",
         "char",
         "varchar2",
         "varchar2",
         "varchar2",
         "number",
         "number",
         "number",
         "number",
         "number",
         "varchar2",
         "char",
         "number",
         "number",
         "number",
         "date",
         "varchar2",
         "char",
         "varchar2"
      ],
      "db_id": "AGENTS",
      "foreign_keys": [
         
            [
               18,1
            ],
            [
               23,7
            ],
            [
               24,1
            ]
         
      ],
      "primary_keys": [
         1,
         7,
         19
      ],
      "table_names": [
         "  ",
         "CUSTOMER",
         "ORDERS"
      ],
      "table_names_original": [
         "AGENTS",
         "CUSTOMER",
         "ORDERS"
      ]
   }










   {
        "db_id": "AGENTS",
        "question": "Show the name of agents and consumers in ascending alphabetical order of the Agent's name.",
        "question_toks": [
            "Show",
            "the",
            "name",
            "of",
            "agents",
            "and",
            "consumers",
            "in",
            "ascending",
            "alphabetical",
            "order",
            "of",
            "the",
            "Agent",
            "'",
            "s",
            "name",
            "."
        ]
    }

'''