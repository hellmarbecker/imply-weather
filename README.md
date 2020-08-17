# imply-weather

Use the weather flow by Tim Spann (https://github.com/tspannhw/ClouderaFlowManagementWorkshop) to push data via Kafka into Imply.

Contains a docker-compose file that deploys:
  - NiFi (Apache OSS)
  - ksqldb (by Confluent)
  - Imply Manager & Agent (by Imply)
  
In the repository, you must create a file named `env.secret` that contains one line:

    IMPLY_MANAGER_LICENSE_KEY=<license_key>
    
where, instead of `<license_key>`, you paste the content of the license file supplied by Imply.

## Setup instructions

### Startup

From the repo directory, run

    docker-compose up -d
    
### Kafka

Note: Kafka broker is externally exposing port 29092. For communication inside docker, use `broker:9092` as the bootstrap address.

Create two topics for the weather data. For instance, using the standard Kafka clients:

    ./kafka-topics.sh --create --topic weather --partitions 1 --bootstrap-server localhost:29092
    ./kafka-topics.sh --create --topic weather-raw --partitions 1 --bootstrap-server localhost:29092
    
### Confluent Schema Registry

Schema Registry is available at `localhost:8081`.

### NiFi

The NiFi GUI is accessible at `localhost:8080`. Upload the template `weather1.xml` and deploy it. Activate all services.

### Imply

Set up a minimal cluster according to https://docs.imply.io/on-prem/deploy/deployment#step-4-deploy-the-rest-of-the-cluster-components.

Configure ingestion from the `weather` topic.

[TBC]
