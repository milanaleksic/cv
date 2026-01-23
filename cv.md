# Milan Aleksić

Last updated: 23/01/2026

## Personal

Born on 21/12/1983, Smederevo (Serbia), living in Koekelberg (Belgium) with my wife and children since 2011. I hold dual citizenship of Belgium and Serbia.

My website is [aleksic.dev](https://aleksic.dev), email is [milan@aleksic.dev](mailto:milan@aleksic.dev) and Twitter account is: [milanaleksic](https://x.com/milanaleksic).
I am fairly active on [github.com/milanaleksic](https://github.com/milanaleksic). My LinkedIn account is [@milanaleksic](https://www.linkedin.com/in/milanaleksic) if you'd like to connect with me.

<details><summary><h2>Education & spoken languages</h2></summary>

Dipl. Ing. Computer Science & Engineering (2008) from the *University of Belgrade* (Serbia), Faculty of Electrical Engineering (ETF). “NARIC – Vlaanderen” [recognized my diploma as M.Sc.](https://aleksic.dev/public/cv-nostrification.pdf).

I speak the following languages: **Serbian** (mother tongue), **English** (fluent), **Dutch** ([C1 Effectiveness 1](https://aleksic.dev/public/cefr_en_overzicht_nt2_aanbod.pdf)), **French** (A2, basic level)

</details>

<details><summary><h2>Keywords</h2></summary>

Java, Go, AWS, Python, PostgreSQL, MySQL, ClickHouse

</details>

<details><summary><h2>Work experience</h2></summary>

<details><summary><h3>[2020-...] Senior Software Engineer @ Soda (remote; HQ in Brussels, Belgium)</h3></summary>

Backend founding engineer of Soda, working on Soda Cloud SaaS. Programming languages I used were Java, Python and Go.

I became the company’s go-to backend engineer and MySQL performance guy. Helped scale the company 100x in both customers and revenue during my tenure in Soda.

I had a multi-hat impact on the organization through domain, infrastructure, and system design as well as providing engineering support and coaching. Some of the most prominent backend features I worked on were internal frameworks for authorization, feature gates, notification rules, database and search query framework, dependency injection, configuration management, OpenAPI code generator, etc. I also participated in the development of many of Soda critical architecture components beside backend: Decrypter, Guardian, Soda Kubernetes Agent, introduction of ClickHouse etc.

I also envisioned and developed an internal devops CLI tool (`dopy` / `dogo`) for automating many painful DevOps tasks. v1 was in Python, v2 in Go (integrating APIs from AWS, Okta, Datadog, Kubernetes, Soda Cloud Admin API, Github).

</details>

<details><summary><h3>[2017-2020] Expert Software Engineer @ TomTom (Ghent, Belgium)</h3></summary>

#### MPU Core Coverage Creation & Extension Team

- *MLF library*: authored code-generated Java wrapper around GDAL OpenFileGDB (later extended to PostGIS and GeoPackage).
  - Custom ANTLR grammar for extended validation and Python/Markdown doc generator
- *Sinatra*: Led migration of a complex process into AWS for GIS source data digestion
  - PostgreSQL RDS, Spring Boot 2, SQS, ECS, Terraform, Vue.js
- *Pupin*: created machine learning cloud service for data classification (plural junctions problem)
  - Training: PostGIS, Python, Scikit-Learn, XGBoost, (Geo)Pandas, Jupyter
  - Online+Batch prediction: Terraform / AWS ECS, Spring Boot 2, XGBoost
- *Dumbo*: migration of internal heavily used batch processing tool into the cloud
  - AWS Batch, ECS, PostgreSQL, S3, X-Ray; Spring Boot 2, Terraform, Python, Jenkins

#### Hermes team

- *Nozem*: always-up-to-date OpenStreetMap ingestion service into core TomTom data layer: Kafka, PostgreSQL, Python, Spring Boot, Jenkins
- *Lego*: automated OpenStreetMap features ingestion: k8s, Python, Java, QGIS plugins

</details>

<details><summary><h3>[2013-2017] {Senior, Lead} Software Engineer @ Basware (Aalst, Belgium)</h3></summary>

Projects:

- *Basware Network Portal*: Full-stack development role on online and internal services
  - Tech stack: Play2, Scala, Java8, MongoDB, Spring, Chef, Go
  - Rewritten core validation business rules implementation (Java)
- *Basware e-Archiving*: DevOps lead-in-charge and one of lead developers
  - Tech stack: CloudFormation, Jenkins, Bash, AWS CLI
  - Cloud stack: Java Lambda functions, API GW, S3, DynamoDB, SQS, Splunk
- *Norsu* (Groovy, Cucumber, Gradle): Cross-systems end-to-end testing
- Business Metrics dashboards (Akka and Dashing.io)
- Migration of legacy Resin applications to Tomcat cluster
  - Oracle, JSP, RMI, Ant, Tomcat, Apache2
- *HAL9000* (Go): Flowdock bot (CI/CD automation helper for 100+ developers)

</details>

<details><summary><h3>[2006-2013] Previous work experience</h3></summary>

<p><footer>Reach out for a chat if you'd like more details about anything listed here.</footer></p>

**2014**: Freelance Consultant (remote) @ Gtech UK (*Brussels, Belgium*)

**2011-2013**: Software consultant @ Cronos (Belgium) (*Brussels, Belgium*)

**2009-2011**: Software Engineer II @ Gtech G2 Sports Betting (*Belgrade, Serbia*)

**2007-2009**: Java Developer @ Arius (*Belgrade, Serbia*)

**2006**: Intern software developer @ ESAProjekt (*Katowice, Poland*)

</details>

<details><summary><h2>Selected open source projects</h2></summary>

- **Advent of Code 2023** (Zig): [github.com/milanaleksic/adventofcode2023](https://github.com/milanaleksic/adventofcode2023)
- **Advent of Code 2018** (Go): [github.com/milanaleksic/adventofcode2018](https://github.com/milanaleksic/adventofcode2018)
- **Personal Web site** (Hugo, Cloudflare Pages): [github.com/milanaleksic/aleksic.dev](https://github.com/milanaleksic/aleksic.dev)

</details>

<details><summary><h2>Selected closed source personal projects</h2></summary>

- **Home Laboratory**: Hybrid cluster: ARM/AMD, Proxmox LXCs/metal, home/Oracle Cloud. Uses Ansible for setup and Kubernetes (k3s) for container scheduling of 40+ services. Deep monitoring via Grafana Stack and Prometheus. Migrated away from Nomad in 2025.
- **Thought Train** (Go, PostgreSQL, NATS, htmx) My main side project – a distributed service for feature-rich web page content extraction, note-taking, and book annotation. Uses an ANTLR search query grammar, R2 as object storage, with mobile apps (Flutter for Android/iOS), and a Chrome Extension (Svelte).
- **Novinarnica** (Go): Content crawler and CBR packager for magazines.
- **kube-home-dns** (Go): k8s controller that is at the same time a home DNS server, a NextDNS forwarder, a Cloudflare DNS record syncer and a Caddy config provider for my k8s-free DMZ ingress

</details>
