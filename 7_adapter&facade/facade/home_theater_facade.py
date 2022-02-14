class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd, cd, projector, lights, screen, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.lights = lights
        self.screen = screen
        self.popper = popper

    def watch_movie(self, movie):
        print('Get ready to watch a movie...')
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_dvd(self.dvd)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print('Shutting movie theater down...')
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

    def listen_to_cd(self, title):
        print('Get ready for an audiopile experence...')
        self.lights.on()
        self.amp.on()
        self.amp.set_volume(5)
        self.amp.set_cd(self.cd)
        self.amp.set_stereo_sound()
        self.cd.on()
        self.cd.play(title)

    def end_cd(self):
        print('Shutting down CD...')
        self.amp.off()
        self.amp.set_cd(self.cd)
        self.cd.eject()
        self.cd.off()

    def listen_to_radio(self, frequency):
        print('Tuning in the airwaves...')
        self.tuner.on()
        self.tuner.set_frequency(frequency)
        self.amp.on()
        self.amp.set_volume(5)
        self.amp.set_tuner(self.tuner)

    def end_radio(self):
        print('Shutting down the tuner...')
        self.tuner.off()
        self.amp.off()
