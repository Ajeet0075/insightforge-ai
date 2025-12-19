from app.agents.analytics_agent import analytics_agent
from app.agents.seo_agent import seo_agent
from app.utils.llm import extract_seo_intent


def handle_query(req):
    """
    Central orchestrator that routes the query to the correct agent.
    MUST NEVER throw an exception.
    """

    query = req.query.strip()

    # 1️⃣ Analytics queries (explicit)
    if getattr(req, "propertyId", None):
        return analytics_agent(query, req.propertyId)

    # 2️⃣ SEO intent detection (SAFE)
    try:
        seo_intent = extract_seo_intent(query)
        issue_type = seo_intent.get("issue_type")
    except Exception:
        issue_type = None  # HARD FAIL SAFE

    if issue_type:
        return seo_agent(query)

    # 3️⃣ Tier-3 safe fallback response
    return {
        "agent": "general",
        "answer": (
            "I can analyze your marketing performance using real data from "
            "Google Analytics and SEO crawls.\n\n"
            "Try asking questions like:\n"
            "- Give me daily page views and users for the last 7 days\n"
            "- Find pages with missing meta descriptions\n"
            "- Show pages with SEO errors or low word count"
        )
    }
