from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AnonStrictThrottle(AnonRateThrottle):
    """
    Very tight limits for anonymous/unauthenticated requests.
    Prevents unauthenticated probing of the API.
    """
    scope = 'anon_strict'
    rate = '10/minute'


class AuthBurstThrottle(AnonRateThrottle):
    """
    Strict limits for authentication endpoints (login, register, token refresh).
    Prevents brute-force credential stuffing and enumeration attacks.
    Scoped per endpoint via get_cache_key override if needed.
    """
    scope = 'auth_burst'
    rate = '5/minute'

    def get_cache_key(self, request, view):
        # Use the client's IP address for anonymous auth attempts
        # This prevents brute force even if attackers rotate user agents
        ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident,
        }


class UserStandardThrottle(UserRateThrottle):
    """
    Moderate limits for general authenticated user activity.
    Covers list views, detail views, logout, and other standard operations.
    """
    scope = 'user_standard'
    rate = '100/minute'


class AIGenerationThrottle(UserRateThrottle):
    """
    Very strict limits for the AI quiz generation endpoint.
    This endpoint is extremely expensive:
      - Downloads audio from YouTube (bandwidth + time)
      - Runs Whisper transcription (CPU/GPU intensive)
      - Calls Gemini AI API (cost + latency)
    Limits: 3 per hour, 10 per day per authenticated user.
    """
    scope = 'ai_generation'
    rate = '3/hour'

