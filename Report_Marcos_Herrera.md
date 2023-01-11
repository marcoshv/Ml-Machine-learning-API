# Flask ML API assignment
## Introduction
    In sprint project 4 a shell of a machine learning API to predict images (image classification models) was given to us by the instructor,
    in this case we had to finish the python scripts to make the API work and deploy the API using docker. The API used a Convolutional Neural network to predict the uploaded images, these images were uploaded into the API using flask and HTML. The API was further tested, all tests had to be passed to consider it ready for deployment.

## Hardware
    Processor: Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz   2.21 GHz
    Installes: RAM: 16.0 GB (15.8 GB usable) DDR4-2400 CL=17
    OS: 64-bit operating system, x64-based processor
    Hard Drive: 512GB NVMe  7400 MB/s read speed /  3400 MB/s write speed

## Tests
    Integration end-to-end --> PASSED
    Api --> 8/8 PASSED
    Model --> PASSED

## Stress Tests
All locust reports were saved in the 'Locust_reports' folder inside the 'stress_test' folder.

                 Number of users       Spawn rate          RPS     Requests   Fails    Response time 100%ile(ms)   time(min)
    Test 1 -            50                 5               5.8        1965      91             7100                   5
    Test 2 -            100                5               5.7        1699      68             17000                  5
    Test 3 -            500                5               5.8        2146      87             88000                  5
    Test 7 -            100                5               5.7        2274      0              16000                  5

### Test scaled services (2 model services)
                 Number of users       Spawn rate          RPS     Requests   Fails    Response time 100%ile(ms)   time(min)
    Test 4 -            50                 5               9.6        3346      173            3500                   5
    Test 5 -            100                5               9.7        3015      171            8900                   5
    Test 6 -            500                5               8.7        2918      145            78000                  5
    

## Final comments
1-The scaled service got a much better performance than the single service, getting higher requests per second(RPS) and less response time in all tests.
2-Errors in the tests are related to the try- except funtion in the ml_service.py script, which allowed me to hardcode the values or class_name and prediction score in case the image was still being used and avoid the model container to close by catching the error.
3- In order to remove the fails a time gap 'time.sleep(0.008)'  was introduced in the ml.service before running the prediction, this eliminated the number fo fails and got the same performance in terms of RPS and RT. This can be seen in the report from test number 7.