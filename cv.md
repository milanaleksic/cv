# Milan Aleksić

Last updated: 02/07/2024

## Personal

Born on 21/12/1983, Smederevo (Serbia), living in Koekelberg (Belgium) since 2011. I have dual citizenship of Belgium and Serbia.

My website is [aleksic.dev](https://aleksic.dev), email is [milan@aleksic.dev](mailto:milan@aleksic.dev) and Twitter account is: [milanaleksic](https://twitter.com/milanaleksic).
I am fairly active on [github.com/milanaleksic](https://github.com/milanaleksic).
I also have a [LinkedIn account](https://www.linkedin.com/in/milanaleksic) if you'd like to connect with me.

<details><summary><h2>Education</h2></summary>

Dipl. Ing. Computer Science & Engineering (2008) from *University of Belgrade* (Serbia), Faculty of Electrical Engineering (ETF)

“NARIC – Vlaanderen” [recognized diploma as M.Sc.](https://aleksic.dev/public/cv-nostrification)

</details>

<details><summary><h2>Spoken languages</h2></summary>

- **Serbian** (mother tongue)
- **English** (fluent)
- **Dutch** ([C1 Effectiveness 1](https://aleksic.dev/public/cefr_en_overzicht_nt2_aanbod.pdf))
- **French** (A2, basic level)

</details>

<details><summary><h2>Keywords</h2></summary>

Java, Go, AWS, Python, PostgreSQL, MySQL

</details>

<details><summary><h2>Experience</h2></summary>

<details><summary><h3>Senior Software Engineer @ Soda (Belgium)</h3></summary>

Place: **Remote/Brussels, Belgium**

Period: **2020-...**

Projects:

- soda.io Cloud Backend (founding) engineer
  + Programming languages: (mostly) Java, Python and cloud development on AWS using Terraform
  + Tasked with backend feature development, guidance and documentation. One of the first ("founding") engineers and therefore I witnessed all the pivoting, market adaptations, surprising platform usage patterns, product evolution, became the company MySQL perf guy, guided or advised all the Soda Cloud development efforts...
  + Helped the company grow 100x in customers and revenue over 5 years without high-profile incidents or downtime of the Soda Cloud product
  + Beyond product and engineering impact, also introduced discipline in performance analysis and monitoring via DataDog, incident management and other operational concerns of the Soda Cloud
- Tool maker role: 
  + deep incident analysis tool using custom dynamically created trace profiles - `datadog-exporter` (Go, Datadog API, SQLite, Perfetto)
  + internal tool for various admin tasks, including feature flip management, admin API back-channel, environment setup, DB dynamic password feneration, framework for complex migrations, etc - `dopy` (Python3, Okta SSO+MFA, boto3) 
- Broad exposure to data sources while helping bootstrap [Soda SQL](https://github.com/sodadata/soda-sql): PostgreSQL, Redshift, Athena, Spark

</details>

<details><summary><h3>Expert Software Engineer @ TomTom (Belgium)</h3></summary>

Place: **Ghent, Belgium**

Period: **2017-2020**

#### CCE Team

Feature development and maintenance of various core systems and applications in *MPU Core Coverage Creation & Extension* team

Projects:

- *MLF library*: authored code-generated Java wrapper around GDAL OpenFileGDB (later extended to PostGIS and GeoPackage).
  + Custom ANTLR grammar for extended validation, Python/Markdown doc generator
- *Sinatra*: Led migration of a complex process into AWS for GIS source data digestion
  + PostgreSQL RDS, Spring Boot 2, SQS, ECS, Terraform, Vue.js
- *Pupin*: created machine learning cloud service for data classification (plural junctions problem)
  + Training: PostGIS, Python, Scikit-Learn, XGBoost, (Geo)Pandas, Jupyter
  + Online+Batch prediction: Terraform / AWS ECS, Spring Boot 2, XGBoost, REST
- *Dumbo*: migration of internal heavily used batch processing tool into the cloud
  + AWS Batch, ECS, PostgreSQL, S3, X-Ray; Spring Boot 2, Terraform, Python, Jenkins
- *Excelsior*: process orchestration service
  + [States Language implementation](https://states-language.net/spec.html) (spec only), ECS+Lambda, Java 11, Python 3

#### Hermes team

Feature development on new long-term systems and applications in *Hermes* team

Projects:

- *Nozem*: always-up-to-date OpenStreetMap ingestion service into core TomTom data layer
  + Kafka, PostgreSQL, Python, Spring Boot, Jenkins
- *Lego*: automated OpenStreetMap features ingestion
  + Kubernetes on Azure Cloud, Python, Java, QGIS Python plugins

</details>

<details><summary><h3>{Senior, Lead} Software Engineer @ Basware (Belgium)</h3></summary>

Place: **Aalst, Belgium**

Period: **2013-2017**

Projects:

- *Basware Network Portal*: Full-stack development role on online and internal services
  + Tech stack: Play2, Scala, Java8, MongoDB, Spring, Chef, Go
  + Rewritten core validation business rules implementation (Java)
- *Basware e-Archiving*: DevOps lead-in-charge and one of lead developers
  + Tech stack: CloudFormation, Jenkins, Bash, AWS CLI
  + Cloud stack: Java Lambda functions, API GW, S3, DynamoDB, SQS, Splunk
- *Norsu* (Groovy, Cucumber, Gradle): Cross-systems end-to-end testing
- Business Metrics dashboards (Akka and Dashing.io)
- Migration of legacy Resin applications to Tomcat cluster
  + Oracle DB, JSP, RMI, Ant, Tomcat, Apache2
- *HAL9000* (Golang): Flowdock bot (CI/CD automation helper for 100+ developers)

</details>
  
<details><summary><h3>Previous work experience</h3></summary>
  
**2014**: Freelance Consultant (remote) @ Gtech UK (_Brussels, Belgium_)

**2011-2013**: Software consultant @ Cronos (Belgium) (_Brussels, Belgium_)
  
**2009-2011**: Software Engineer II @ Gtech G2 Sports Betting (_Belgrade, Serbia_)

**2007-2009**: Java Developer @ Arius (_Belgrade, Serbia_)

**2006**: Intern software developer @ ESAProjekt (_Katowice, Poland_)

</details>

<details><summary><h2>Selected open source projects</h2></summary>

- [Advent of Code 2023](https://github.com/milanaleksic/adventofcode2023) (Zig)
- [Github Helper CLI](https://github.com/milanaleksic/ghh) (Rust, Github API)
  + epic issues dependency graph handling, branch names and other "my flow" helpers
- [Personal Web site](https://github.com/milanaleksic/man-website) (Hugo, Cloudflare Pages)
- [Advent of Code 2018](https://github.com/milanaleksic/adventofcode2018) (Go)
- [gomakefiles](https://github.com/milanaleksic/gomakefiles) (Makefile, Bash)
  + Reusable Makefile files which allow cross CI/CD Go compilation with many useful tools
- [Igor](https://github.com/milanaleksic/igor) (Go Lambda, Vue.js, Google+, CloudFront, Cognito, DynamoDB)
  + “I am away” Flowdock bot, deployed via Semaphore.ci + CloudFormation

</details>

<details><summary><h2>Selected closed source personal projects</h2></summary>

- Home Laboratory
  + Hybrid cluster (aarch64/amd64 debian/ubuntu, home/Oracle cloud) connected using Tailscale. NAS included
  + Infra as code: Ansible for foundational setup of bare new nodes, Nomad/Consul for container scheduling (25+ services like Gitea, Minecraft, yarr, etc.)
  + Monitoring via Grafana, InfluxDB, Grafana Loki and Tempo
- Thought Train (Go, PostgreSQL, ANTLR, NATS, Vue.js / htmx, Svelte, Flutter, Bootstrap)
  + Feature-rich web page content extraction & book annotation distributed service
  + Search Query grammar, Pulumi-based AWS cloud setup
  + mobile applications (Android, iOS) and Chrome Extension
- Batler (Go)
  + Telegram bot I use for home automation tasks like turning on/off my workhorse laptop, Windows VM and main notification pipeline
- Novinarnica (Go, Google OAuth, Batler)
  + Content crawler and CBR packager of magazines from www.novinarnica.net

</details>

<details><summary><h2>Miscellaneous</h2></summary>

### Public talks

- (BeScala) [Introducing a reactive Scala-Akka based system in a Java centric company](http://www.meetup.com/BeScala/events/220967046/) with Jeroen Verellen, 2015

</details>
