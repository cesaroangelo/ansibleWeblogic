connect('weblogic','weblogic','t3://localhost:7001')
target='AdminServer'
 
line1='/opt/oracle/sites/CS'
line2='CS'
 
line3='/opt/oracle/sites/cas'
line4='cas'
 
undeploy(appName=line2,path=line1, targets=target)
undeploy(appName=line4,path=line3, targets=target)

