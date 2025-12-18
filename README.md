# Spike AI Analytics Agent

Backend-only AI system that answers natural-language questions using:
- Google Analytics 4 (GA4 Data API)
- Agent-based orchestration

## API
POST /query

```json
{
  "propertyId": "GA4_PROPERTY_ID",
  "query": "Natural language question"
}
