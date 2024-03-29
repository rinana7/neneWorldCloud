import numpy
from matplotlib import pyplot
from PIL import Image
from wordcloud import WordCloud

WORD = """
Nene’s Birthday Wish. In the heart of Meadowbrook, where dandelions danced and fireflies whispered secrets, lived Nene. 
Her cottage nestled among wildflowers, and her days were painted with simplicity. On her birthday, Nene received a 
lavender-scented note: “Follow the dandelion path.” Curious, she followed it to a glade adorned with fairy lights. Lila, 
the baker, and Jasper, the artist, awaited her. They sang, laughed, and shared stories. But the true magic lay in a 
wooden box—a silver key to the wishing well. Nene closed her eyes, wished for eternal laughter, and unlocked the well. 
Fireflies emerged, swirling like stardust. Nene knew this day was a gift—a promise to cherish friendship, sunsets, and 
vanilla-scented dreams. Happy birthday, dear Nene. May your wishes bloom forever.
"""
IMAGE_MASK_PATH = "./nene_mask.png"
IMAGE_OUTPUT_PATH = "./nene.png"

alice_mask = numpy.array(Image.open(IMAGE_MASK_PATH))
wc = WordCloud(
    background_color="white",
    mask=alice_mask,
)
wc.generate(WORD)
wc.to_file(IMAGE_OUTPUT_PATH)

pyplot.imshow(wc)
pyplot.axis("off")
pyplot.show()
