from PIL import Image 
from rembg import remove
import aspose.words as aw


def jpg_a_png(path_in, path_out):
  path_input = f"./img/{path_in}.jpg"
  path_output = f"./img/{path_out}.png"
  foto = Image.open(path_input)
  salida = remove(foto)
  salida.save(path_output)

def png_a_svg(path_in, path_out):
  path_input = f"./img/{path_in}.png"
  path_output = f"./img/{path_out}.svg"
  doc = aw.Document()
  builder = aw.DocumentBuilder(doc)
  shape = builder.insert_image(path_input)
  shape.get_shape_renderer().save(path_output, aw.saving.ImageSaveOptions(aw.SaveFormat.SVG))