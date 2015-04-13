import cairocffi as cairo

width = 500
height = 500


surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)
center = (width / 2, height / 2)

context.set_operator(cairo.OPERATOR_CLEAR)
context.paint()

context.set_operator(cairo.OPERATOR_SOURCE)
context.set_antialias(cairo.ANTIALIAS_BEST)

context.set_source_rgb(0, 0, 0)
context.set_font_face(cairo.ToyFontFace("Steelfish"))
context.set_font_size(60)
context.move_to(200, 200)
context.show_text("SampleSteelTag")

surface.flush()
surface.write_to_png("./img.png")
surface.finish()

print(center)