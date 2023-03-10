# Apheris test - Mattia Spinelli

## Start the system
`docker-compose up --build -d`

NOTE: you will see some error messages from the currywurst_service and the storage_service, untill rabbitMQ is fully running. This is because of some limitation of docker-compose and the depends_on functionality.  


## Buy a currywurst
Navigate to [localhost:80/docs](localhost:80/docs)

You will be able to create a post request from there. 


## Check the logs
The storage_service uses the filesystem to store the logs. There is a mounted volume to ensure persistance. Logs will be in `apheris-test/storage_service/db.logs.txt`


## Time to complete
I did this over 2 days, but I wasn't fully dedicated to it. Probably 4/5 the first day and 3 hours the next day. 