# SentinelLogs 
Intelligent Log Monitoring, Anomaly Detection & Alerting System SentinelLogs is an intelligent monitoring platform that analyzes application logs in real time,
detects anomalous behavior, and generates actionable alerts before incidents impact users.
The project is inspired by real-world monitoring tools (Grafana, Datadog, Prometheus) and focuses on how alerts are detected, managed, and visualized, not just logged.

## The Problem
 **Modern applications generate thousands of logs per day:**
 * Errors are hidden inside log noise
   
 * Manual log inspection is slow and unreliable
   
 * Alerts are often triggered after outages
   
### Without intelligent monitoring, teams:
 * React instead of preventing incidents

 * Lose time debugging production issues

 * Lack visibility into application behavior

## What SentinelLogs Solves
**SentinelLogs continuously analyzes metrics derived from logs and provides:**

* Early anomaly detection

* Severity-based alerting

* Real-time dashboard visibility

* Alert history & lifecycle tracking

 ## Core Features
 ###Metrics Monitoring

* Logs per minute

* Error rate tracking

* Time-series aggregation

### Anomaly Detection
* Log volume spikes
  
* Error rate spikes
  
* Baseline comparison

* Dynamic severity scoring (LOW → CRITICAL)

### Alerting Engine
* Rule-based alerts

* Severity thresholds

* Cooldown & deduplication

###Alert lifecycle:
* OPEN (active anomaly)

* RESOLVED (anomaly disappeared)

### Dashboard
* Metrics summary

* Live charts

* Active alerts panel (shown only when alerts exist)

* Alert history (historique)

* Clean UI with Tailwind CSS and nextJS
