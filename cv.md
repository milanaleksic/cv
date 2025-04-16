# Milan Aleksić

Last updated: 16/04/2025

## Personal

Born on 21/12/1983, Smederevo (Serbia), living in Koekelberg (Belgium) since 2011. I have dual citizenship of Belgium and Serbia.

My website is [aleksic.dev](https://aleksic.dev), email is [milan@aleksic.dev](mailto:milan@aleksic.dev) and Bluesky account is: [aleksic.dev](https://bsky.app/profile/aleksic.dev).
I am fairly active on [github.com/milanaleksic](https://github.com/milanaleksic).
I also have a [LinkedIn account](https://www.linkedin.com/in/milanaleksic) if you'd like to connect with me.

<details><summary><h2>Education & spoken languages</h2></summary>

Dipl. Ing. Computer Science & Engineering (2008) from *University of Belgrade* (Serbia), Faculty of Electrical Engineering (ETF). “NARIC – Vlaanderen” [recognized my diploma as M.Sc.](https://aleksic.dev/public/cv-nostrification).

I can speak in the following languages: **Serbian** (mother tongue), **English** (fluent), **Dutch** ([C1 Effectiveness 1](https://aleksic.dev/public/cefr_en_overzicht_nt2_aanbod.pdf)), **French** (A2, basic level)

</details>

<details><summary><h2>Keywords</h2></summary>

Java, Go, AWS, Python, PostgreSQL, MySQL

</details>

<details><summary><h2>Work experience</h2></summary>

<details><summary><h3>[2020-...] Senior Software Engineer @ Soda (remote; HQ in Brussels, Belgium)</h3></summary>

My role was soda.io Cloud Backend founding engineer (since late spring 2025 also a member of the Foundation team). Programming languages I used were Java, Python and Go.

I became the company backend guy & MySQL perf guy and helped the company grow 100x in customers and revenue over 5 years without high-profile incidents of the Soda Cloud product. I had a multi-hat impact on org through domain, infra and system design. Maintainer of Soda k8s agent, Vault Decrypter, warehouse source preparation, public API, OpenAPI generator, custom DI/DB framework and other complex features and mini-services.

I made an internal platform CLI tool (`dopy` / `dogo`) for many painful DevOps automation tasks - v1 Python, v2 Go (APIs from AWS/Okta/Datadog/k8s/soda cloud, SQLite, Perfetto).

</details>

<details><summary><h3>[2017-2020] Expert Software Engineer @ TomTom (Ghent, Belgium)</h3></summary>

#### MPU Core Coverage Creation & Extension Team

- *MLF library*: authored code-generated Java wrapper around GDAL OpenFileGDB (later extended to PostGIS and GeoPackage).
  + Custom ANTLR grammar for extended validation and Python/Markdown doc generator
- *Sinatra*: Led migration of a complex process into AWS for GIS source data digestion
  + PostgreSQL RDS, Spring Boot 2, SQS, ECS, Terraform, Vue.js
- *Pupin*: created machine learning cloud service for data classification (plural junctions problem)
  + Training: PostGIS, Python, Scikit-Learn, XGBoost, (Geo)Pandas, Jupyter
  + Online+Batch prediction: Terraform / AWS ECS, Spring Boot 2, XGBoost
- *Dumbo*: migration of internal heavily used batch processing tool into the cloud
  + AWS Batch, ECS, PostgreSQL, S3, X-Ray; Spring Boot 2, Terraform, Python, Jenkins

#### Hermes team

- *Nozem*: always-up-to-date OpenStreetMap ingestion service into core TomTom data layer: Kafka, PostgreSQL, Python, Spring Boot, Jenkins
- *Lego*: automated OpenStreetMap features ingestion: k8s, Python, Java, QGIS plugins

</details>

<details><summary><h3>[2013-2017] {Senior, Lead} Software Engineer @ Basware (Aalst, Belgium)</h3></summary>

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
  + Oracle, JSP, RMI, Ant, Tomcat, Apache2
- *HAL9000* (Go): Flowdock bot (CI/CD automation helper for 100+ developers)

</details>
  
<details><summary><h3>[2006-2013] Previous work experience</h3></summary>

<p><footer>Reach out for a chat if you want more details about things in this list.</footer></p>
  
**2014**: Freelance Consultant (remote) @ Gtech UK (_Brussels, Belgium_)

**2011-2013**: Software consultant @ Cronos (Belgium) (_Brussels, Belgium_)
  
**2009-2011**: Software Engineer II @ Gtech G2 Sports Betting (_Belgrade, Serbia_)

**2007-2009**: Java Developer @ Arius (_Belgrade, Serbia_)

**2006**: Intern software developer @ ESAProjekt (_Katowice, Poland_)

</details>

<details><summary><h2>Selected open source projects</h2></summary>

- Advent of Code 2023: [github.com/milanaleksic/adventofcode2023](https://github.com/milanaleksic/adventofcode2023) (Zig)
- Personal Web site: [github.com/milanaleksic/aleksic.dev](https://github.com/milanaleksic/aleksic.dev) (Hugo, Cloudflare Pages)
- Advent of Code 2018: [github.com/milanaleksic/adventofcode2018](https://github.com/milanaleksic/adventofcode2018) (Go) 

</details>

<details><summary><h2>Selected closed source personal projects</h2></summary>

- Home Laboratory: a hybrid cluster (arm/amd, RPis/NUC Proxmox/Synology NAS, home/Oracle Cloud) connected using Tailscale. Uses Ansible for foundational setup and HashiCorp Nomad for container scheduling (40+ services like Gitea, Minecraft, yarr, etc.). Deep monitoring via Grafana Stack and InfluxDB. Slowly migrated to k3s.
- Thought Train (Go, PostgreSQL, NATS, htmx) my main side project: a feature-rich web page content extraction, note taking & book annotation distributed service; utilizes an ANTLR Search Query grammar, Pulumi AWS and with dedicated mobile applications (Android, iOS, using Flutter) and a Chrome Extension (Svelte)
- Batler (Go): personal Telegram bot I use for homelab automation tasks and as the main notification pipeline
- Novinarnica (Go): content crawler and CBR packager of magazines

</details>

