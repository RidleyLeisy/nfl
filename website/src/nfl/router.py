from rest_framework import routers
from frontend.api.views import *

router = routers.DefaultRouter()
router.register('games', GamesReadView, basename='games')
router.register('playsflat', PlaysFlatReadView, basename='playsflat')
router.register('teams', TeamStatsReadView, basename='teams')
router.register('player', PlayerPositionReadView, basename='player')
