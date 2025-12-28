from google.adk.agents.llm_agent import Agent
from datetime import datetime

# Timezone support: try stdlib zoneinfo first, fall back to pytz if necessary
try:
    from zoneinfo import ZoneInfo

    def _now_in_timezone(tz_name: str) -> datetime:
        return datetime.now(ZoneInfo(tz_name))
except Exception:
    try:
        import pytz

        def _now_in_timezone(tz_name: str) -> datetime:
            return datetime.now(pytz.timezone(tz_name))
    except Exception:
        def _now_in_timezone(tz_name: str) -> datetime:
            raise RuntimeError("Timezone support not available. Use Python 3.9+ or install 'pytz'.")

# Common city -> tz database name mapping (keys are lowercase)
CITY_TIMEZONES = {
    'new york': 'America/New_York',
    'los angeles': 'America/Los_Angeles',
    'san francisco': 'America/Los_Angeles',
    'london': 'Europe/London',
    'paris': 'Europe/Paris',
    'berlin': 'Europe/Berlin',
    'tokyo': 'Asia/Tokyo',
    'sydney': 'Australia/Sydney',
    'mumbai': 'Asia/Kolkata',
    'delhi': 'Asia/Kolkata',
    'kolkata': 'Asia/Kolkata',
    'shanghai': 'Asia/Shanghai',
    'beijing': 'Asia/Shanghai',
    'seoul': 'Asia/Seoul',
    'singapore': 'Asia/Singapore',
    'dubai': 'Asia/Dubai',
    'moscow': 'Europe/Moscow',
    'toronto': 'America/Toronto',
    'vancouver': 'America/Vancouver',
}


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Accepts common city names (e.g., "New York", "Tokyo") or a tz database
    name (e.g., "Europe/London"). Returns a dict with status and formatted time.
    """
    if not city or not city.strip():
        return {"status": "error", "error": "no city provided", "supported": list(CITY_TIMEZONES.keys())}

    key = city.strip().lower()
    tz_name = CITY_TIMEZONES.get(key)
    # If not a known city, assume user supplied a tz DB name
    if tz_name is None:
        tz_name = city.strip()

    try:
        dt = _now_in_timezone(tz_name)
    except Exception as e:
        return {
            "status": "error",
            "error": "timezone_lookup_failed",
            "message": str(e),
            "supported_examples": list(CITY_TIMEZONES.keys())[:10],
        }

    formatted = dt.strftime("%I:%M %p").lstrip('0')
    return {
        "status": "success",
        "city": city,
        "timezone": tz_name,
        "time": formatted,
        "iso": dt.isoformat(),
        "utc_offset": dt.strftime('%z'),
    }


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)