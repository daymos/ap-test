# Apheris test - Mattia Spinelli


## Run the tests
You need to have the api dependancies and pytest installed in your shell. From the root of the repo run:
`python3 -m pytest`

I added 2 integration tests as a token. Ideally, more and more meaningfull scenarios should be tested.

There are no unit test, but the business logic layer could be easily tested. 


## Start the system
`docker-compose up --build -d`

NOTE: you will see some error messages from the currywurst_service and the storage_service, untill rabbitMQ is fully running. This is because of some limitation of docker-compose and the depends_on functionality.  


## Buy a currywurst and documentation
Navigate to [localhost:3003/docs](localhost:3003/docs). 

You should see interactive documentation for the api. You will be able to create a post request from there. 


## Check the logs
The storage_service container uses the filesystem to store the events. There is a mounted volume to ensure persistance betweeen runs. Data will be in `apheris-test/storage_service/db/logs.txt`.
This is not a choice  would do in production, but am just conscious of time. A Redis like DB would have worked there as well.
In order to connect the records to a specific api request, I'm generating a correlation id in the middleware of the api, and use that as primary key of the event data structure.


## Monitor the queue
Navigate to [http://localhost:15672/](rabbitMQ admin dashboard). 


## Time to complete
I did this over 2 days, but I wasn't fully dedicated to it. Probably 4/5 the first day and 3/4 hours the next day. 