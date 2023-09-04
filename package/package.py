# 패키지

## 패키지 만들기

# export PYTHONPATH="/.../python"
import game.sound.echo
game.sound.echo.echo_test() # >>> 'echo'

# $ python3
from game.sound import echo
echo.echo_test() # >>> 'echo'

from game.sound.echo import echo_test
echo_test() # >>> 'echo'

import game
game.sound.echo.echo_test()

# 패키지 하위를 접근할 수 없다
# import package.game
# package.game.sound.echo.echo_test()

import game
game.sound.echo.echo_test()

# __all__
from game.sound import *
echo.echo_test()

from game.graphic.render import render_test
render_test()