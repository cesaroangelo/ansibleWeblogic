connect('weblogic','weblogic','t3://localhost:7001')
cd ('AppDeployments')
myapps=cmo.getAppDeployments()

for appName in myapps:
           domainConfig()
           cd ('/AppDeployments/'+appName.getName()+'/Targets')
           mytargets =ls(returnMap='true')
           cd('domainRuntime:/AppRuntimeStateRuntime/AppRuntimeStateRuntime')
           for targetinst in mytargets:
                     curstate=cmo.getCurrentState(appName.getName(),targetinst)
                     print appName.getName(), '=', curstate
 
