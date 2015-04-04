import cairocffi as cairo

class TagCloudService:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.center = (self.width / 2, self.height / 2)
        self.spiral_room = 0
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        self.context = cairo.Context(self.surface)

    def construct(self):
        self.prepare_surface()
        self.context.set_source_rgb(0, 0, 0)
        self.context.set_font_face(cairo.ToyFontFace("Steelfish"))
        self.context.set_font_size(60)
        self.context.move_to(200, 200)
        self.context.show_text("SampleSteelTag")

        self.surface.flush()
        self.surface.write_to_png("./img.png")

    def prepare_surface(self):
        self.context.set_operator(cairo.OPERATOR_CLEAR)
        self.context.paint()
        self.context.set_operator(cairo.OPERATOR_SOURCE)
        self.context.set_antialias(cairo.ANTIALIAS_BEST)

