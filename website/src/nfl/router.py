from rest_framework import routers
from frontend.api.views import *

router = routers.DefaultRouter()
router.register('games', GamesReadView, basename='games')
router.register('teams', TeamStatsReadView, basename='teams')
router.register('player', PlayerPositionReadView, basename='player')
router.register('offense', OffenseReadView, basename='offense')
router.register('passing', PassingReadView, basename='passing')
router.register('touchdowns', TouchdownReadView, basename='touchdowns')