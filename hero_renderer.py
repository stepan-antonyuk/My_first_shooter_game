class UniverseRenderer:
    def __init__(self, renderer):
        self.renderer = renderer
        self.hero_renderers = {
            'standing': StandingHeroRenderer(renderer),
            'jumping': JumpingHeroRenderer(renderer),
            'crouching': CrouchingHeroRenderer(renderer),
        }

    def render_hero(self, hero):
        renderer = self.hero_renderers[hero.state]
        renderer.render_hero(hero)

# abstract
class HeroRenderer:
    def __init__(self, renderer):
        self.renderer = renderer

    def render_hero(self, hero):
        pass


class StandingHeroRenderer(HeroRenderer):
    def __init__(self, renderer):
        super(HeroRenderer, self).__init__(renderer)

    def render_hero(self, hero):
        pass


class JumpingHeroRenderer(HeroRenderer):
    def __init__(self, renderer):
        super(HeroRenderer, self).__init__(renderer)

    def render_hero(self, hero):
        pass


class CrouchingHeroRenderer(HeroRenderer):
    def __init__(self, renderer):
        super(HeroRenderer, self).__init__(renderer)

    def render_hero(self, hero):
        pass
