# Hai Tran 13 JUN 2022
# Setup flask

from flask import Flask, render_template

app = Flask(__name__)

# get book list should be even number
books = [
    {
        "title": "Simplify Big Data Analytics with Amazon EMR",
        "author": "Sakti Mishra",
        "image": "https://d2cvlmmg8c0xrp.cloudfront.net/web-css/singapore.jpg",
        "description": "Amazon EMR, formerly Amazon Elastic MapReduce, provides a managed Hadoop cluster in Amazon Web Services (AWS) that you can use to implement batch or streaming data pipelines. By gaining expertise in Amazon EMR, you can design and implement data analytics pipelines with persistent or transient EMR clusters in AWS.This book is a practical guide to Amazon EMR for building data pipelines. You will start by understanding the Amazon EMR architecture, cluster nodes, features, and deployment options, along with their pricing. Next, the book covers the various big data applications that EMR supports. You will then focus on the advanced configuration of EMR applications, hardware, networking, security, troubleshooting, logging, and the different SDKs and APIs it provides. Later chapters will show you how to implement common Amazon EMR use cases, including batch ETL with Spark, real time streaming with Spark Streaming, and handling UPSERT in S3 Data Lake with Apache Hudi. Finally, you will orchestrate your EMR jobs and strategize on premises Hadoop cluster migration to EMR. In addition to this, you will explore best practices and cost optimization techniques while implementing your data analytics pipeline in EMR",
    },
    {
        "title": "Simplify Big Data Analytics with Amazon EMR",
        "author": "Sakti Mishra",
        "image": "https://d2cvlmmg8c0xrp.cloudfront.net/web-css/singapore.jpg",
        "description": "Amazon EMR, formerly Amazon Elastic MapReduce, provides a managed Hadoop cluster in Amazon Web Services (AWS) that you can use to implement batch or streaming data pipelines. By gaining expertise in Amazon EMR, you can design and implement data analytics pipelines with persistent or transient EMR clusters in AWS.This book is a practical guide to Amazon EMR for building data pipelines. You will start by understanding the Amazon EMR architecture, cluster nodes, features, and deployment options, along with their pricing. Next, the book covers the various big data applications that EMR supports. You will then focus on the advanced configuration of EMR applications, hardware, networking, security, troubleshooting, logging, and the different SDKs and APIs it provides. Later chapters will show you how to implement common Amazon EMR use cases, including batch ETL with Spark, real time streaming with Spark Streaming, and handling UPSERT in S3 Data Lake with Apache Hudi. Finally, you will orchestrate your EMR jobs and strategize on premises Hadoop cluster migration to EMR. In addition to this, you will explore best practices and cost optimization techniques while implementing your data analytics pipeline in EMR",
    },
    {
        "title": "Simplify Big Data Analytics with Amazon EMR",
        "author": "Sakti Mishra",
        "image": "https://d2cvlmmg8c0xrp.cloudfront.net/web-css/singapore.jpg",
        "description": "Amazon EMR, formerly Amazon Elastic MapReduce, provides a managed Hadoop cluster in Amazon Web Services (AWS) that you can use to implement batch or streaming data pipelines. By gaining expertise in Amazon EMR, you can design and implement data analytics pipelines with persistent or transient EMR clusters in AWS.This book is a practical guide to Amazon EMR for building data pipelines. You will start by understanding the Amazon EMR architecture, cluster nodes, features, and deployment options, along with their pricing. Next, the book covers the various big data applications that EMR supports. You will then focus on the advanced configuration of EMR applications, hardware, networking, security, troubleshooting, logging, and the different SDKs and APIs it provides. Later chapters will show you how to implement common Amazon EMR use cases, including batch ETL with Spark, real time streaming with Spark Streaming, and handling UPSERT in S3 Data Lake with Apache Hudi. Finally, you will orchestrate your EMR jobs and strategize on premises Hadoop cluster migration to EMR. In addition to this, you will explore best practices and cost optimization techniques while implementing your data analytics pipeline in EMR",
    },
    {
        "title": "Simplify Big Data Analytics with Amazon EMR",
        "author": "Sakti Mishra",
        "image": "https://d2cvlmmg8c0xrp.cloudfront.net/web-css/singapore.jpg",
        "description": "Amazon EMR, formerly Amazon Elastic MapReduce, provides a managed Hadoop cluster in Amazon Web Services (AWS) that you can use to implement batch or streaming data pipelines. By gaining expertise in Amazon EMR, you can design and implement data analytics pipelines with persistent or transient EMR clusters in AWS.This book is a practical guide to Amazon EMR for building data pipelines. You will start by understanding the Amazon EMR architecture, cluster nodes, features, and deployment options, along with their pricing. Next, the book covers the various big data applications that EMR supports. You will then focus on the advanced configuration of EMR applications, hardware, networking, security, troubleshooting, logging, and the different SDKs and APIs it provides. Later chapters will show you how to implement common Amazon EMR use cases, including batch ETL with Spark, real time streaming with Spark Streaming, and handling UPSERT in S3 Data Lake with Apache Hudi. Finally, you will orchestrate your EMR jobs and strategize on premises Hadoop cluster migration to EMR. In addition to this, you will explore best practices and cost optimization techniques while implementing your data analytics pipeline in EMR",
    },
]


@app.route("/")
def index():
    return render_template(
        "index.html", books=books, nrow=len(books) // 2
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
