s_manager = None
screens = dict()


def switch_screen(screen, dirct):
    s_manager.switch_to(screens[screen], direction=dirct)
