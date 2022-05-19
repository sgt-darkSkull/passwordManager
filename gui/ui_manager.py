class UiManager:

    s_manager = None
    screens = dict()

    def switch_screen(self,  screen, direction):
        self.s_manager.switch_to(self.screens[screen], direction=direction)
