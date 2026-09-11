from rest_framework.throttling import UserRateThrottle

class auraRateThrottle(UserRateThrottle):
    scope = 'aura'