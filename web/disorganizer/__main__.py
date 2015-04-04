__author__ = 'Home'
from disorganizer import freetype_font_cairo
import cairocffi as cairo

width = 500
height = 500

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)
context.set_antialias(cairo.ANTIALIAS_BEST)
center = (width / 2, height / 2)
context.set_operator(cairo.OPERATOR_CLEAR)
context.paint()

face = freetype_font_cairo.create_cairo_font_face_for_file("Y:/Vasaz/Repos/Confidence/web/disorganizer/Steelfish.ttf", 0)

surface.flush()
surface.write_to_png("./img.png")
surface.finish()

print(center)