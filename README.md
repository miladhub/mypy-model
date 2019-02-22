Python I/O redirection with Docker example
===

Toy project experimenting how to use a Python app inside a Docker container to stream commands via STDIN
and receive responses via STDOUT just like you would do with a local Python app.

Each line in STDIN is interpreted as a Base64-encoded JSON string containing the model inputs.

This might help in deciding how to invoke apps embedded with Docker.

Building the Docker image
===

    docker build -t mypy .

Invoking it
===

The following command prints file `input.json` 10 times onto STDIN, encodes each of them via Base 64 and feeds the result to the model:

    $ seq 1 10 | xargs -I{} sh -c "cat input.json | base64" | docker run --rm -i mypy
    {"score": [{"Date_Time": "2017-07-30 12:05:00", "Predicted_Temperature": 29.961414831320837}, {"Date_Time": "2017-07-30 12:10:00", "Predicted_Temperature": 30.02936509060561}, {"Date_Time": "2017-07-30 12:15:00", "Predicted_Temperature": 30.201606037722854}, {"Date_Time": "2017-07-30 12:20:00", "Predicted_Temperature": 30.204359454268854}, {"Date_Time": "2017-07-30 12:25:00", "Predicted_Temperature": 30.046219875248795}, {"Date_Time": "2017-07-30 12:30:00", "Predicted_Temperature": 30.03961423865934}, {"Date_Time": "2017-07-30 12:35:00", "Predicted_Temperature": 30.157289798825246}, {"Date_Time": "2017-07-30 12:40:00", "Predicted_Temperature": 30.400845008340156}, {"Date_Time": "2017-07-30 12:45:00", "Predicted_Temperature": 30.56468920944036}, {"Date_Time": "2017-07-30 12:50:00", "Predicted_Temperature": 30.664924338250472}, {"Date_Time": "2017-07-30 12:55:00", "Predicted_Temperature": 30.59871479351105}, {"Date_Time": "2017-07-30 13:00:00", "Predicted_Temperature": 30.628119156333923}]}
    ...
    {"score": [{"Date_Time": "2017-07-30 12:05:00", "Predicted_Temperature": 29.961414831320837}, {"Date_Time": "2017-07-30 12:10:00", "Predicted_Temperature": 30.02936509060561}, {"Date_Time": "2017-07-30 12:15:00", "Predicted_Temperature": 30.201606037722854}, {"Date_Time": "2017-07-30 12:20:00", "Predicted_Temperature": 30.204359454268854}, {"Date_Time": "2017-07-30 12:25:00", "Predicted_Temperature": 30.046219875248795}, {"Date_Time": "2017-07-30 12:30:00", "Predicted_Temperature": 30.03961423865934}, {"Date_Time": "2017-07-30 12:35:00", "Predicted_Temperature": 30.157289798825246}, {"Date_Time": "2017-07-30 12:40:00", "Predicted_Temperature": 30.400845008340156}, {"Date_Time": "2017-07-30 12:45:00", "Predicted_Temperature": 30.56468920944036}, {"Date_Time": "2017-07-30 12:50:00", "Predicted_Temperature": 30.664924338250472}, {"Date_Time": "2017-07-30 12:55:00", "Predicted_Temperature": 30.59871479351105}, {"Date_Time": "2017-07-30 13:00:00", "Predicted_Temperature": 30.628119156333923}]}

As a result, the output JSON prediction will be printed out 10 times on STDOUT.
