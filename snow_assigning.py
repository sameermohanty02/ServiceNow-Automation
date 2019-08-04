
import pysnow
import re
c = pysnow.Client(instance='instance', user='username', password='password')
incident = c.resource(api_path='/table/incident')


#using the same assigment group above to fetch more tickets
qb = (
    pysnow.QueryBuilder()
    .field("assignment_group").equals(<id>)
    .AND()
    .field( "priority").equals("3")
	.OR()
	.field( "priority").equals("4")
	.OR()
	.field( "priority").equals("5")
)

response = incident.get(query=qb)
filter = re.compile(r'Network|WAN|LAN',re.IGNORECASE)
filter1 = re.compile(r'Linux',re.IGNORECASE)
filter2 = re.compile(r'Windows',re.IGNORECASE)



for b in response.all():
 print (str(b['description']))
 result = filter.search(str(b['description']))
 if result:
  update = {'assignment_group' : 'NETWORK Queue'}
  updated_record = incident.update(query={'number': b['number']}, payload=update)
  print (b['number'],"Network Queue")
 elif result is None:
  result = filter1.search(str(b['description']))
  if result:
   update = {'assignment_group' : 'Linux Queue'}
   updated_record = incident.update(query={'number': b['number']}, payload=update)
   print (b['number'],"Linux Queue")
  else:
   result = filter2.search(str(b['description']))
   if result:
    update = {'assignment_group' : 'Windows Queue'}
    updated_record = incident.update(query={'number': b['number']}, payload=update)
    print (b['number'],"Windows Queue")
   print(b['number'], "- can't find queue")
  
   
   





