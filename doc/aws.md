# About AWS(Amazon Web Service)

## AWS Management Console

## EC2

### Connct to the instance using SSH

## Amazon Route 53

## IAM (Identity and Access Management)
- a web service that helps you securely control access to AWS resources.
- control who is authenticated (signed in) and authorized (has permissions) to use resources
- AWS account *root user* : signing in whith the email address and password

## CloudFront
## CloudWatch

## Lambda

## Amazon VPC(Virtual Private Cloud)


## AWS Storage Service

### Which AWS Cloud Storage Service Is Best
- Amazon S3 is cheapest for data storage alone. However, there are various other pricing parameters in S3, including cost per number of requests made, S3 Analytics, and data transfer out of S3 per gigabyte. EFS has the simplest cost structure. 

- Amazon S3 can be accessed from anywhere. AWS EBS is only available in a particular region, while you can share files between regions on multiple EFS instances.

- EBS and EFS are both faster than Amazon S3, with high IOPS and lower latency

- EBS is scalable up or down with a single API call. Since EBS is cheaper than EFS, you can use it for database backups and other low-latency interactive applications that require consistent, predictable performance.

- EFS is best used for large quantities of data, such as large analytic workloads. Data at this scale cannot be stored on a single EC2 instance allowed in EBS—requiring users to break up data and distribute it between EBS instances. The EFS service allows concurrent access to thousands of EC2 instances, making it possible to process and analyze large amounts of data seamlessly.
