My first postmortem: Unexpected Service Disruption on My App.

Issue Summary
- Duration: June 9, 2024. 14:00–18:30 (GMT)
- Impact: My Airbnb clone web app experienced intermittent outages, affecting approximately 30% of users during peak hours.
- Root Cause: A misconfigured load balancer caused excessive traffic to a critical database server.

Timeline
- 14:00: Monitoring alerts triggered due to increased latency in authentication requests.
- 14:15: I noticed elevated error rates and began investigating.
- 14:30: Initial assumption: Database performance issue. I focused on query optimization.
- 15:00: Misleading path: Optimized database queries, but the issue persisted.
- 16:00: Escalated the issue to me (as the infrastructure team).
- 17:00: Load balancer logs revealed the misconfiguration.
- 18:30: I corrected the load balancer settings, restoring service just in time.

Root Cause and Resolution
- Cause: The load balancer was misconfigured to route all traffic to a single database server, overwhelming it.
- Resolution: I corrected the load balancer settings to distribute traffic evenly across database replicas.

Corrective and Preventative Measures
Load Balancer Configuration:
- Improvement: Implement automated checks for load balancer settings.
- Task: I will periodically create a script to validate load balancer configurations.

Database Replication:
- Improvement: Increase database replicas to handle higher loads.
- Task: I will provision additional read replicas and update failover procedures.

Monitoring Enhancements:
- Improvement: Enhance monitoring to detect misconfigurations.
- Task: I will set up alerts for load balancer anomalies and database performance.

Incident Response Training:
- Improvement: Ensure I understand escalation paths.
- Task: I will conduct regular incident response drills.

Documentation Update:
- Improvement: Document load balancer best practices.
- Task: I will add load balancer configuration guidelines.

By implementing these measures, the aim is to improve the resilience of the system and minimize the impact of any future service disruptions.
