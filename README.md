#Service Now Automation using Resful APIs

## SNOW_CLOSING.yml

In this File I have used ansible to close tickets based on ICMP checks on the hosts.

if the Ping is 100%, the automation will go ahead and close the tickets. 

Please note the below points:

- Use only the Instance name and not the entire URL of the service now.
- This uses only the ping command to run on the host. ICMP module is a different module altogether in Ansible.
- Uses Regex to search the output.

## SNOW_FILTERING.py

This is a python file which uses Restful APIs to filter out tickets based on its short description.

Based on its short description the automation would assign tickets to its respective queues.

Please note the below points:

- I have used the existing Pysnow module.
- While using qb(query builder which acts are a filter) you need to use ID of the assignement group and not the assignment group name itself.
- But while assigning tickets you should use the group name.
