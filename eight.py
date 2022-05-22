#8
import json
def json_prog():
   sampleJson ="""{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
            }
         }
      }
   }"""

   data=json.loads(sampleJson)

   print(data["company"]["employee"]["payble"]["salary"])
json_prog()