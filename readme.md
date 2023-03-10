# Apheris test - Mattia Spinelli

## Start the system
`docker-compose up --build -d`

NOTE: you will see some error messages from the currywurst_service and the storage_service, untill rabbitMQ is fully running. This is because of some limitation of docker-compose and the depends_on functionality.  


## Buy a currywurst
Navigate to [localhost:80/docs](localhost:3003/docs)

You will be able to create a post request from there. 


## Check the logs
The storage_service container uses the filesystem to store the events. There is a mounted volume to ensure persistance betweeen runs. Data will be in `apheris-test/storage_service/db.logs.txt`.
This is not a choice  would do in production, but am just conscious of time. A Redis like DB would have worked there as well, if one is going to query by correlationId.


## Time to complete
I did this over 2 days, but I wasn't fully dedicated to it. Probably 4/5 the first day and 3 hours the next day. 