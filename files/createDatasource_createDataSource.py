from java.io import FileInputStream

propInputStream = FileInputStream("details.properties")
configProps = Properties()
configProps.load(propInputStream)

domainName=configProps.get("domain.name")
adminURL=configProps.get("admin.url")
adminUserName=configProps.get("admin.userName")
adminPassword=configProps.get("admin.password")

dsName=configProps.get("datasource.name")
dsFileName=configProps.get("datasource.filename")
dsDatabaseName=configProps.get("datasource.database.name")
datasourceTarget=configProps.get("datasource.target")
dsJNDIName=configProps.get("datasource.jndiname")
dsDriverName=configProps.get("datasource.driver.class")
dsURL=configProps.get("datasource.url")
dsUserName=configProps.get("datasource.username")
dsPassword=configProps.get("datasource.password")
dsTestQuery=configProps.get("datasource.test.query")

connect(adminUserName, adminPassword, adminURL)
edit()
startEdit()
cd('/')
cmo.createJDBCSystemResource(dsName)
cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName)
cmo.setName(dsName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
set('JNDINames',jarray.array([String(dsName )], String))

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName )
cmo.setUrl(dsURL)
cmo.setDriverName( dsDriverName )
cmo.setPassword(dsPassword)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName )
cmo.setTestTableName(dsTestQuery)
cmo.setConnectionReserveTimeoutSeconds(25)
cmo.setMaxCapacity(100)
cmo.setConnectionReserveTimeoutSeconds(10)
cmo.setTestFrequencySeconds(120)
set('TestConnectionsOnReserve', 'true')

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
cmo.createProperty('user')

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/user')
cmo.setValue(dsUserName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
cmo.createProperty('databaseName')

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/databaseName')
cmo.setValue(dsDatabaseName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
cmo.setGlobalTransactionsProtocol('OnePhaseCommit')

cd('/SystemResources/' + dsName )
set('Targets',jarray.array([ObjectName('com.bea:Name=' + datasourceTarget + ',Type=Server')], ObjectName))

save()
activate()

